from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from gameDockApp.models import Pedido, Producto
from gameDockApp.models import Pedido
from gameDockApp.models import Producto_Pedido
from gameDockApp.carrito import Carrito
from django.contrib.auth.models import User
from gameDockApp.forms import RegisterForm
from gameDockApp.forms import PedidoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import braintree
from django.core.mail import EmailMessage

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

def pedidos(request):
  pedidos = Pedido.objects.all()
  pedido = None
  id_pedido = request.GET.get('id-pedido', '0')
  if id_pedido:
    pedido = [p for p in pedidos if p.ID_Seguiment() == id_pedido][0]
    return elegir_metodo_pago(request, pedido.pk)
  return render(request, 'pedidos.html')

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

def elegir_metodo_pago(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    datos_pedido = Producto_Pedido.objects.filter(pedido=pedido)
    total = pedido.total_pedido()
    
    return render(request, 'tramitar_pedido.html', {'datos_pedido': datos_pedido, 'pedido': pedido, 'total': total,'MEDIA_URL': settings.MEDIA_URL})

def crear_nuevo_pedido(request):
    if request.method == 'POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid:
            try:
                pedido = crear_pedido(request, formulario)
            except:
                mess = messages.add_message(request, level=0, message='Información inválida')
                return render(request, 'pedido_form.html', {'formulario': formulario, 'messages':mess})
            return redirect('/pedidos/?id-pedido={}'.format(pedido.ID_Seguiment()))
        else:
            mess = messages.add_message(request, level=0, message='Información inválida')
            return render(request, 'pedido_form.html', {'formulario': formulario, 'messages':mess})
    else:
        formulario = PedidoForm()
    return render(request, 'pedido_form.html', {'formulario': formulario})

def crear_pedido(request, formulario):
    usuario = request.user
    if usuario.is_authenticated:
        pedido = Pedido(usuario=usuario)
    else:
        pedido = Pedido()
    pedido.nombre =  formulario['nombre'].value()
    pedido.codigo_postal = formulario['codigo_postal'].value()
    pedido.email =  formulario['email'].value()
    pedido.direccion = formulario['direccion'].value()
    pedido.estado_pedido = pedido.EstadoPedido.EN_TIENDA
    pedido.pagado = False
    pedido.braintree_id = None
    pedido.save()
    carrito = Carrito(request)
    for key, value in carrito.carrito.items():
        id_producto = value.get("id_producto")
        producto = get_object_or_404(Producto, pk=id_producto)
        nuevo_producto_pedido = Producto_Pedido(pedido=pedido, producto=producto, cantidad=value.get("cantidad"))
        nuevo_producto_pedido.save()
    return pedido

##PEDIDO:
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request, id_pedido):
    pedido = get_object_or_404(Pedido, pk=id_pedido)
    coste = pedido.total_pedido()
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{coste:.2f}',
            'payment_method_nonce': nonce,
            'options': {
            'submit_for_settlement': True
            }
        })
        if result.is_success:
        # mark the order as paid
            pedido.pagado = True
            # store the unique transaction id
            pedido.braintree_id = result.transaction.id
            pedido.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request,
            'payment/process.html',
            {'pedido': pedido,
            'client_token': client_token
            })

def payment_done(request):
    return render(request, 'payment_done.html')

def payment_canceled(request):
    return render(request, 'payment_canceled.html')

def register(request):
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        if formulario.is_valid:
            try:
                usuario = formulario.save()
            except:
                mess = messages.add_message(request, level=0, message='Información inválida')
                return render(request, 'register.html', {'formulario': formulario, 'messages':mess})
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


def politica_envio(request):
    return render(request, "politica_envio.html")

def contrarreembolso(request):
  email_client(request)
  return render(request, 'contrareembolso.html')

def email_client(request):

  #obtener name, email y message de los datos puestos por el cliente

  name = 'name'
  email = 'jicastro1999@gmail.com'
  message = 'Codigo pedido'

  mail = EmailMessage(
    'Mensaje recibido',
    'Sent by {} <{}>\n\n{}'.format(name,email,message),
    email,
    ['e52ad75676853e@inbox.mailtrap.io'],
    reply_to=[email],
  )

  '''send_mail(
    subject = 'Test Mail',
    message = 'Kindly Ignore',
    from_email = email,
    recipient_list = ['e52ad75676853e@inbox.mailtrap.io',],
    fail_silently = False,
  )'''

  return render(request, 'contrareembolso.html')