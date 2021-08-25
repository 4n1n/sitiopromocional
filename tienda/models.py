from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.
class PRODUCTS(models.Model):
    id_producto=models.CharField(max_length=3,primary_key=True)
    nombredelproducto=models.CharField(max_length=50) 
    proveedor=models.CharField(max_length=50)
    cantidad=models.IntegerField()

class CATEGORIES(models.Model):
    id_producto=models.CharField(max_length=3,)
    categoria=models.CharField(max_length=20)


class DISCOUNT (models.Model):
    id_producto=models.CharField(max_length=5,primary_key= True)
    precio=models.CharField (max_length=10)
    descuento=models.PositiveIntegerField (default=5)
    PRODUCTS=models.ForeignKey(PRODUCTS,null=False,blank=False,on_delete=models.CASCADE)



