from django.shortcuts import render, get_object_or_404
from django.conf import settings
from gameDockApp.models import Producto
from haystack.query import SearchQuerySet

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
    return render(request, 'product_detail.html', {'producto': producto, 'MEDIA_URL': settings.MEDIA_URL})

def search_titles(request):
  productos = SearchQuerySet().autocomplete(content_auto = request.POST.get('search_text', ''))
  return render_to_response('ajax_search.html', {'productos': productos})