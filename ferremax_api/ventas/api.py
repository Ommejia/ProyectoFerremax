from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, CartItem
from .serializadores import ProductSerializer, CartItemSerializer

class ProductListAPI(ListAPIView):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer

class CartItemListCreateAPI(ListAPIView, CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get('products', [])
        response_data = []
        selected_product_ids = []  # Lista para almacenar IDs de productos seleccionados
        total = 0
        try:
            for item in data:
                product = Product.objects.get(id=item['id'])
                cart_item = CartItem.objects.create(product=product, quantity=item['quantity'])
                response_data.append(CartItemSerializer(cart_item).data)
                total += product.price * item['quantity']
                # Agregar ID del producto seleccionado a la lista
                selected_product_ids.append(product.id)
            return Response({'message': 'Productos añadidos al carro de compras', 'cart_items': response_data, 'total': total, 'selected_product_ids': selected_product_ids}, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({'error': 'Solicitud inválida'}, status=status.HTTP_400_BAD_REQUEST)

class CheckoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        CartItem.objects.all().delete()
        return Response({'message': 'Pago realizado con éxito'}, status=status.HTTP_200_OK)
