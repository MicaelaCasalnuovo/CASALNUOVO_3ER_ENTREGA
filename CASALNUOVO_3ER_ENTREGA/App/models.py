from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)

class Sku(models.Model):
    sku = models.IntegerField()  
    descripcion = models.CharField(max_length=30)
    
class Stock(models.Model):
    sku = models.IntegerField() 
    descripcion = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    recio = models.IntegerField()

class Factura(models.Model):
    fecha_fc = models.DateField()
    nro_fc = models.CharField(max_length=16)  
    sku = models.IntegerField()  
    cantidad = models.IntegerField()
    precio = models.IntegerField()