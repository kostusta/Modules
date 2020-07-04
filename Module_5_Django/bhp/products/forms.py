from django import forms

from products import models


class NewProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'description', 'price', 'image', 'stock_quantity')


class EditProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'description', 'price', 'image', 'stock_quantity')


#class NewPurchaseForm(forms.ModelForm):
#    class Meta:
#        model = models.Purchase
#        fields =
