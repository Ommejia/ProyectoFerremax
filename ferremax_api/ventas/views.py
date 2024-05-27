from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def products_api(request):
    if request.method == 'GET':
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['POST', 'GET'])
def cart_api(request):
    if request.method == 'POST':
        try:
            data = request.data
            products = data.get('products', [])
            for item in products:
                product = Product.objects.get(id=item['id'])
                CartItem.objects.create(product=product, quantity=item['quantity'])
            return Response({'message': 'Productos añadidos al carro de compras'}, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Solicitud inválida'}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        cart = serializer.data
        total = sum(item['product']['price'] * item['quantity'] for item in cart)
        return Response({'products': cart, 'total': total})

@csrf_exempt
@api_view(['POST'])
def checkout_api(request):
    if request.method == 'POST':
        CartItem.objects.all().delete()
        return Response({'message': 'Pago realizado con éxito'}, status=status.HTTP_200_OK)
