from django.db.models.query import QuerySet
from django.http.request import QueryDict
from tienda.models import CATEGORIES, PRODUCTS, DISCOUNT
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, OrderBy, Min, Max, Avg
# Create your views here.


def inicio(request):
    return render(request, 'tienda/inicio.html', {})
# Comento la def simple
# def productos(request):
#    return render(request, 'tienda/productos.html', {})


def productos(request):
    # Creo variable donde almaceno todos los objetos PRODUCTS
    listaproductos = PRODUCTS.objects.all()
    # La vista productos va a devolver en la url registrada, un objeto oproductos con el contenido de la variable listaproductos
    return render(request, 'tienda/productos.html', {"oproductos": listaproductos})


def detalle(request):
    return render(request, 'tienda/detalles.html', {})


def dashboard(request):
    datos = {}
    categorias = CATEGORIES.objects.all()
    productos = PRODUCTS.objects.all()
    categorias_productos = {}
    for categoria in categorias:
        categorias_productos[categoria.descripcion] = 0
    # print(categorias_productos)
    for producto in productos:
        if (producto.categoria.descripcion in categorias_productos):
            categorias_productos[producto.categoria.descripcion] += 1
    # print(categorias_productos)
    datos['categorias'] = categorias
    datos['productos'] = productos
    datos['categorias_productos'] = categorias_productos
    return render(request, 'tienda/dashboard.html', {"datos": datos})

def prueba(request):
    datos = {}
    productos = PRODUCTS.objects.all()
    descuentos = DISCOUNT.objects.all()
    descuentos_productos = {}
    for descuento in descuentos:
        descuentos_productos[descuento.descripcion] = 0
    for producto in productos:
        if (producto.descuento.descripcion in descuentos_productos):
            descuentos_productos[producto.descuento.descripcion] +=1
    datos['descuentos'] = descuentos
    datos['productos'] = productos
    datos['categorias_descuentos'] = descuentos_productos
    return render(request, 'tienda/prueba.html', {"datos": datos})