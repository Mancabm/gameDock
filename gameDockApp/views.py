from django.shortcuts import render, get_object_or_404
from django.conf import settings
from gameDockApp.models import Producto

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    return render(request,'cliente_principal.html', {'productos':productos})

def product_detail(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    return render(request, 'product_detail.html',{'producto': producto, 'MEDIA_URL': settings.MEDIA_URL})

