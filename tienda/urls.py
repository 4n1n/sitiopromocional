from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='bienvenidos'),
    path('productos/', views.productos, name='productos'),
    path('detalle/', views.detalle,name='detalles_producto'),
    path('dashboard/', views.dashboard,name='dashboard'),
]