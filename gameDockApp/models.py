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
    precio = models.FloatField(help_text="Precio del producto")
    stock = models.IntegerField(help_text="Stock del prodcuto")
    tipo = models.IntegerField(choices=TipoProducto.choices, default=TipoProducto.JUEGO)

    def __str__(self) -> str:
        return self.nombre

class Carrito(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField()

    def __str__(self) -> str:
        return str(self.cliente)

class Pedido(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(help_text="Cantidad del producto comprado")
    entregado = models.BooleanField()

    def ID_seguimiento(self) -> str:
        return hash(self.carrito.date_creation) + hash(self.carrito.cliente.username) + hash(self.producto.nombre)

    def __str__(self) -> str:
        return str(self.carrito) + " "+ str(self.producto)