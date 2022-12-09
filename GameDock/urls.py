"""GameDock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gameDockApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.clientePrincipal, name='Home'),

    path('products/product/<int:id_producto>', views.product_detail),
    path('tratamiento_datos/', views.tratamiento_datos),
    path('pedidos/', views.pedidos),
    path('producto/<int:id>/', views.productos_filtrados),
    path('products/product/<int:id_producto>', views.product_detail, name='Prod'),
    path('limpiar/', views.limpiar_carrito, name='Clear'),
    path('agregar/<int:id_producto>', views.agregar_producto, name='Add'),
    path('decrementar/<int:id_producto>', views.decrementar_producto, name='Dec'),
    path('pedidos/new', views.crear_nuevo_pedido, name='Init_Process'),
    path('pedidos/<int:id_pedido>', views.elegir_metodo_pago, name='DetallePedido'),
    path('pedidos/pago/<int:id_pedido>', views.pago_con_tarjeta, name='PagoPedido'),
    path('pedido_cancelado/', views.pago_cancelado),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('register', views.register),
    path('politica_envio', views.politica_envio),
    path('pedido_realizado', views.pedido_realizado),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
