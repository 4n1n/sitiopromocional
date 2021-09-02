from django.db.models.query import QuerySet
from django.http.request import QueryDict
from tienda.models import CATEGORIES, PRODUCTS, DISCOUNT
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count,OrderBy,Min,Max,Avg
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
    prodxcat=PRODUCTS.objects.all()
    return render(request, 'tienda/dashboard.html', {})

def prueba (request):
    #productoscaros=PRODUCTS.objects.all().order_by('precio') [:3]   
    #return render(request,'tienda/prueba.html', {"oproductoscaros":productoscaros})
    #variables Vista Categorías por Cant. de Productos
    cat = CATEGORIES.objects.all()
    nro_prod = CATEGORIES.objects.annotate(Count('products'))
    vnro_prod = vars(nro_prod)
    #variables Vista Ofertas por Cant. de Productos
    prod_tipodeoferta=DISCOUNT.objects.annotate(Count('products'))
    ofertaprod=DISCOUNT.objects.all()
    #variables Vista Categoría con su Máximo Descuento.
    discxcat=CATEGORIES.objects.annotate(Max('products__descuento__porcentaje')).OrderBy(-'products__descuento__porcentaje')
    #envío todos los objetos al template
    return render(request,'tienda/prueba.html', {"ocat":cat,
                "onroproductos":nro_prod,
                "otipof":prod_tipodeoferta,"oofert":ofertaprod})