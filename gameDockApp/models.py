from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Producto(models.Model):
    class TipoProducto(models.IntegerChoices):
        JUEGO = 1, _('Juego')
        CONSOLA = 2, _('Consola')
        PERIFERICO = 3, _('Periferico')
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(help_text="Descripción del producto")
    precio = models.FloatField(help_text="Precio del producto", null=False)
    stock = models.IntegerField(help_text="Stock del prodcuto", null=False)
    tipo = models.IntegerField(choices=TipoProducto.choices, default=TipoProducto.JUEGO)

    def __str__(self) -> str:
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(help_text="Cantidad del producto comprado", null=False)
    completado = models.BooleanField()

    def __str__(self) -> str:
        return str(self.cliente) + " "+ str(self.producto)