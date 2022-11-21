from django.contrib import admin
from gameDockApp.models import Producto, Pedido, Producto_Pedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Producto_Pedido)