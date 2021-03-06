from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.

class CATEGORIES(models.Model):
    #id_categoria=models.AutoField(primary_key=True)
    descripcion=models.CharField(null=False,default="",max_length=200)
    #cantidad_de_articulos=models.PositiveIntegerField(null=False)

class DISCOUNT(models.Model):
    #id_descuento=models.AutoField(primary_key=True)
    descripcion=models.CharField(null=False,default="",max_length=200)
    porcentaje=models.DecimalField(null=False,default=0,max_digits=8,decimal_places=2)

class PRODUCTS(models.Model):
    #id_producto=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=50) 
    precio=models.DecimalField (max_digits=10,decimal_places=2)
    proveedor=models.CharField(max_length=50)
    categoria=models.ForeignKey(CATEGORIES,on_delete=models.CASCADE)
    descuento=models.ForeignKey(DISCOUNT,on_delete=models.CASCADE)

