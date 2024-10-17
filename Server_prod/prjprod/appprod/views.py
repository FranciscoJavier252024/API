from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def producto_detalle(request):
    producto_id = request.GET.get('id')
    producto = Producto.objects.filter(id=producto_id).first()
    return render(request, 'appprod/producto_detalle.html', {'producto': producto})