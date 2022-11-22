from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from gameDockApp.models import Producto
from gameDockApp.carrito import Carrito

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})

#muestra los títulos de los productos que están registrados filtrados por tipo
def productos_filtrados(request, id):
    productos=Producto.objects.filter(tipo=id)
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})

def product_detail(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    return render(request, 'product_detail.html',{'producto': producto, 'MEDIA_URL': settings.MEDIA_URL})


def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.agregar(producto)
    return redirect("Home")

def eliminar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.eliminar(producto)
    return redirect(request, "Home")

def decrementar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.add(producto)
    return redirect(request, "Home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Home")