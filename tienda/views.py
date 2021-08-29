from tienda.models import PRODUCTS
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def inicio (request):
    return render(request, 'tienda/inicio.html', {})
# Comento la def simple
#def productos(request):
#    return render(request, 'tienda/productos.html', {}) 
def productos(request):
    #Creo variable donde almaceno todos los objetos PRODUCTS
    listaproductos=PRODUCTS.objects.all()
    #La vista productos va a devolver en la url registrada, un objeto oproductos con el contenido de la variable listaproductos
    return render(request, 'tienda/productos.html', {"oproductos":listaproductos})

def detalle (request):
    return render(request, 'tienda/detalles.html', {})

def dashboard (request):
    return render(request, 'tienda/dashboard.html', {})

