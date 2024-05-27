from django.urls import path
from .api import ProductListAPI, CartItemListCreateAPI, CheckoutAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name='product_list_api'),
    path('cart/', CartItemListCreateAPI.as_view(), name='cart_item_list_create_api'),
    path('checkout/', CheckoutAPI.as_view(), name='checkout_api'),
]
