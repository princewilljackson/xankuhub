from django.urls import path

from . import views
app_name = 'products'
urlpatterns = [
    path('products/', views.products, name='product'),
    path('products_list/', views.product_detail, name='products'),
    path('product_descriptions/', views.product_description, name='product_description'),
    path('product_owner/', views.product_owner, name='product_owner'),
    path('owner_detail/', views.owner_contact, name='owner_detail')
]