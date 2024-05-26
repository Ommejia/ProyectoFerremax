from django.urls import path
from ventas.api import VentasAPI

urlpatterns_ventas_api = [
    path(f'ventas/',VentasAPI.as_view())
]
