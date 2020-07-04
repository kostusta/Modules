from django.urls import path

from products import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_page'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/new', views.NewProductView.as_view(), name='new_product'),
    path('products/edit/<int:pk>', views.EditProductView.as_view(), name='edit_product'),
    path('purchase', views.PurchaseListView.as_view(), name='purchases_list'),
    path('refunds', views.RefundsListView.as_view(), name='refunds_list')
]
