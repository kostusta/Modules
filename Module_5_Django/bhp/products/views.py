from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from products import models as product_models, forms
from users import models as user_models


class ProductListView(ListView):
    model = product_models.Product
    queryset = product_models.Product.objects.all()
    template_name = 'products/products_list.html'
    ordering = 'name'

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id', '')
        amount = int(request.POST.get('amount', ''))
        user_id = int(request.POST.get('user_id', ''))

        user = user_models.User.objects.get(pk=user_id)
        product = product_models.Product.objects.get(pk=product_id)

        product.stock_quantity -= amount
        user.wallet -= amount * product.price

        if product.stock_quantity < 0 or user.wallet < 0:
            return render(request, 'products/warning_page.html', {'product': product, 'user': user})
        else:
            purchase = product_models.Purchase(user_id=user, product_id=product, amount=amount)
            user.save()
            product.save()
            purchase.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ProductDetailView(DetailView):
    model = product_models.Product


class NewProductView(CreateView):
    model = product_models.Product
    form_class = forms.NewProductForm
    success_url = reverse_lazy('product_list_page')


class EditProductView(UpdateView):
    model = product_models.Product
    form_class = forms.EditProductForm
    success_url = reverse_lazy('product_list_page')


class PurchaseListView(ListView):
    model = product_models.Purchase
    ordering = 'created_at'
    template_name = 'products/purchase_list.html'

    def get_queryset(self):
        return product_models.Purchase.objects.filter(user_id=self.request.user)

    def post(self, request, *args, **kwargs):
        purchase_id = request.POST.get('purchase_id', '')
        purchase = product_models.Purchase.objects.get(pk=purchase_id)
        if 'refund' in request.POST:
            purchase.make_refund_status = True
            purchase.save()
            refund = product_models.Refund(purchase_id=purchase)
            refund.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class RefundsListView(ListView):
    model = product_models.Refund
    queryset = product_models.Refund.objects.all()
    ordering = 'created_at'
    template_name = 'products/refunds_list.html'

    def post(self, request, *args, **kwargs):
        refund_id = request.POST.get('refund_id', '')
        refund = product_models.Refund.objects.get(pk=refund_id)
        if 'reject' in request.POST:
            refund.confirmation = False
        elif 'approve' in request.POST:
            refund.confirmation = True
            refund.purchase_id.user_id.wallet += refund.purchase_id.amount * refund.purchase_id.product_id.price
            refund.purchase_id.user_id.save()
            refund.purchase_id.product_id.stock_quantity += refund.purchase_id.amount
            refund.purchase_id.product_id.save()
        refund.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
