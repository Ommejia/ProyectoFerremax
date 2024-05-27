from django.urls import path
from ventas.api import ProductListAPI, CartItemListCreateAPI, CheckoutAPI

urlpatterns_ventas_api = [
    # path(f'ventas/',VentasAPI.as_view()),
    path('products/', ProductListAPI.as_view(), name='product_list_api'),
    path('cart/', CartItemListCreateAPI.as_view(), name='cart_item_list_create_api'),
    path('checkout/', CheckoutAPI.as_view(), name='checkout_api'),
]
