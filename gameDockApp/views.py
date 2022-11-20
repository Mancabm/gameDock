from django.shortcuts import render

from gameDockApp.models import Producto
from haystack.query import SearchQuerySet
from django.shortcuts import render_to_response, render

#muestra los títulos de los productos que están registrados
def clientePrincipal(request):
    productos=Producto.objects.all()
    return render(request,'clientePrincipal.html', {'productos':productos})

def search_titles(request):
  productos = SearchQuerySet().autocomplete(content_auto = request.POST.get('search_text', ''))
  return render_to_response('ajax_search.html', {'productos': productos})