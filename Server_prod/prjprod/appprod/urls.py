from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, producto_detalle

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detalle/', producto_detalle, name='producto_detalle'),
]


