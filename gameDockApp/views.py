from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from gameDockApp.models import Producto
from gameDockApp.models import Pedido
from gameDockApp.models import Producto_Pedido
from gameDockApp.carrito import Carrito

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    busqueda = request.GET.get("busqueda")
    if busqueda:
      productos=Producto.objects.filter(nombre__icontains = busqueda)
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})

#muestra los títulos de los productos que están registrados filtrados por tipo
def productos_filtrados(request, id):
    productos=Producto.objects.filter(tipo=id)
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})

def tratamiento_datos(request):
    return render(request,'tratamiento_datos.html')

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
    return redirect("Home")

def decrementar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.decrementar(producto)
    return redirect("Home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Home")

def elegir_metodo_pago(request):
    total = 0
    pedido = Pedido.objects.create()
    carrito = Carrito(request)
    for key, value in carrito.carrito.items():
        id_producto = value.get("id_producto")
        producto = get_object_or_404(Producto, pk=id_producto)
        nuevo_producto_pedido = Producto_Pedido(carrito=pedido, producto=producto, cantidad=value.get("cantidad"))
        nuevo_producto_pedido.save()
        total += value.get('precio') * value.get('cantidad')
    datos_pedido = Producto_Pedido.objects.filter(carrito=pedido)
    return render(request, 'tramitar_pedido.html', {'pedido': pedido, 'total': total,'datos_pedido': datos_pedido, 'MEDIA_URL': settings.MEDIA_URL})
    

