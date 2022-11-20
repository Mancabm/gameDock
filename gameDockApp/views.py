from django.shortcuts import render

from gameDockApp.models import Producto

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    return render(request,'cliente_principal.html', {'productos':productos})