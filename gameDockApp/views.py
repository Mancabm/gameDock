from django.shortcuts import render
from GameDock import settings

from gameDockApp.models import Producto

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})

def productos_filtrados(request, id):
    productos=Producto.objects.filter(tipo=id)
    return render(request,'cliente_principal.html', {'productos':productos, 'MEDIA_URL': settings.MEDIA_URL})