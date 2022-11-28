from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import hashlib
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
    imagen = models.ImageField(upload_to="productos", verbose_name="Productos")

    def __str__(self) -> str:
        return self.nombre

class Pedido(models.Model):
    date_creation = models.DateTimeField(auto_now=True)

    def ID_Seguiment(self)->str:
        return hashlib.sha256(str(self.id).encode('utf-8')).hexdigest()

    def __str__(self) -> str:
        return self.ID_Seguiment()

class Producto_Pedido(models.Model):
    carrito = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(help_text="Cantidad del producto comprado")

    @classmethod
    def create(cls, id_pedido, datos):
        carrito = id_pedido
        producto = datos.get("id_producto")
        cantidad = datos.get("cantidad")
        """ añadir atributo¿? -> 
            total = datos.get("precio") * cantidad  """
        return cls(carrito, producto, cantidad)

    def __str__(self) -> str:
        return str(self.carrito) + " "+ str(self.producto)