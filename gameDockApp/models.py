from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import pgcrypto
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
    class EstadoPedido(models.IntegerChoices):
        EN_TIENDA = 1, _('En Tienda')
        EN_REPARTO = 2, _('En Reparto')
        ENVIADO = 3, _('Enviado')
    date_creation = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = pgcrypto.EncryptedCharField(max_length=150)
    codigo_postal = pgcrypto.EncryptedCharField(max_length=100)
    direccion = pgcrypto.EncryptedTextField()
    email = pgcrypto.EncryptedEmailField()
    estado_pedido = pgcrypto.EncryptedIntegerField(choices=EstadoPedido.choices, default=EstadoPedido.EN_TIENDA)
    pagado = models.BooleanField(default=False)
    braintree_id = pgcrypto.EncryptedCharField(max_length=150, blank=True)
    
    def ID_Seguiment(self)->str:
        return hashlib.sha256(str(self.id).encode('utf-8')).hexdigest()

    def __str__(self) -> str:
        return self.ID_Seguiment()

    def total_pedido(self):
        total = 0
        datos_pedido = Producto_Pedido.objects.filter(pedido=self)
        for d in datos_pedido:
            total += d.producto.precio * d.cantidad
        return total
class Producto_Pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(help_text="Cantidad del producto comprado")


    def __str__(self) -> str:
        return str(self.carrito) + " "+ str(self.producto)