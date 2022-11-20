from gameDockApp.models import Producto
from haystack import indexes

class ProductoIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document = True, use_template = True)
  content_auto = indexes.EdgeNgramField(model_attr = 'nombre')

  def get_model(self):
    return Producto
  
  def index_queryset(self, using = None):
    return self.get_model().objects.all()
