import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremax_api.settings')
django.setup()

from ventas.models import Product

products_db = [
    {"id": 1, "marca": "Bosh", "name": "Taladro Percutor Bosch", "price": 100000, "active": True},
    {"id": 2, "marca": "Hyundai", "name": "Tronzadora eléctrica 2400W", "price": 150000, "active": True},
    {"id": 3, "marca": "Bosh", "name": "Esmeril angular eléctrico 710 W + 7 Discos", "price": 34000, "active": True},
    {"id": 4, "marca": "Bauker", "name": "Sierra circular eléctrica 7 1300W", "price": 39000, "active": True},
    {"id": 5, "marca": "Bauker", "name": "Fresadora Eléctrica 550W", "price": 85990, "active": True},
    {"id": 6, "marca": "Uberman", "name": "Set 400 accesorios para taladro", "price": 29990, "active": True},
]

for product in products_db:
    Product.objects.create(
        marca=product["marca"],
        name=product["name"],
        price=product["price"],
        active=product["active"],
    )
