from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Product, CartItem
import json

def products_api(request):
    if request.method == 'GET':
        products = Product.objects.filter(active=True).values('id', 'marca', 'name', 'price')
        return JsonResponse(list(products), safe=False)

@csrf_exempt
def cart_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            products = data.get('products', [])
            for item in products:
                product = Product.objects.get(id=item['id'])
                CartItem.objects.create(product=product, quantity=item['quantity'])
            return JsonResponse({'message': 'Productos añadidos al carro de compras'})
        except (Product.DoesNotExist, KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest('Solicitud inválida')
    elif request.method == 'GET':
        cart_items = CartItem.objects.all()
        cart = [
            {
                'id': item.product.id,
                'marca': item.product.marca,
                'name': item.product.name,
                'price': item.product.price,
                'quantity': item.quantity
            }
            for item in cart_items
        ]
        total = sum(item['price'] * item['quantity'] for item in cart)
        return JsonResponse({'products': cart, 'total': total})

@csrf_exempt
def checkout_api(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
        return JsonResponse({'message': 'Pago realizado con éxito'})
