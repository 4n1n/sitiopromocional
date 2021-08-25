from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def inicio (request):
    return render(request, 'tienda/inicio.html', {})

def productos(request):
    return render(request, 'tienda/productos.html', {}) 

def detalle (request):
    return render(request, 'tienda/detalles.html', {})

def dashboard (request):
    return render(request, 'tienda/dashboard.html', {})

