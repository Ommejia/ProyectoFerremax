from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView

class VentasAPI(ListAPIView): 
    queryset = modelo.objects.all()
    serializer_class = asd.

    def get(self, request, *args, **kwargs):
        #colocar el proceso de negocio colocar la capa servicio, cuando se ejecuta una venta se invoca venta
        return super().get(request, *args, **kwargs) 