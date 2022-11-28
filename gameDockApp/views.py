from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from gameDockApp.models import Producto
from gameDockApp.carrito import Carrito
from gameDockApp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def register(request):
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        if formulario.is_valid:
            usuario = formulario.save()
            login(request, usuario)
            return redirect("Home")
        else:
            mess = messages.add_message(request, level=0, message='Información inválida')
            return render(request, 'register.html', {'formulario': formulario, 'messages':mess})
    elif request.user.is_authenticated:
        return redirect("Home")
    else:
        formulario = RegisterForm()
    return render(request, 'register.html', {'formulario': formulario})

def log_in(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=usuario, password=password)
            if access is not None:
                login(request, access)
                return redirect("Home")
            else:
                mess = messages.add_message(request, message='Credenciales no válidos', level=0)
                return render(request, 'login.html', {'formulario': formulario, 'messsages': mess})
    elif request.user.is_authenticated:
        return redirect("Home")
    else:
        formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})

@login_required(login_url="/login")
def log_out(request):
    logout(request)
    return redirect("Home")