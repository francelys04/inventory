from django.db import models
from django.utils import timezone


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_bs = models.FloatField()
    precio_us = models.FloatField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    stock_max = models.PositiveIntegerField()
    stock_min = models.PositiveIntegerField()
    cantidadTotal = models.PositiveIntegerField()


#class Transaccion:
#	producto = models.ForeignKey(Producto)
#	tipo = models.CharField(max_length=100)
#	cantidad = models.PositiveIntegerField()
#	total_monto = models.FloatField()
#	fecha_creacion = models.DateTimeField(
 #           default=timezone.now)

#class PrecioDolar:
#	precio = models.FloatField()

