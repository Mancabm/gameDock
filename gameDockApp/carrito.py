class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session.get("carrito")
        else:
            self.carrito = carrito
        

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "id_producto": id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1
            }
        else:
            nueva_cantidad = self.carrito[id].get("cantidad") + 1
            self.carrito[id]["cantidad"] = nueva_cantidad
        self.save()


    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True


    def eliminar(self, producto):
        id = str(producto.id)
        del self.carrito[id]
        self.save()

    def decrementar(self, producto):
        id = str(producto.id)
        nueva_cantidad = self.carrito[id].get("cantidad") - 1
        if nueva_cantidad < 1:
            self.eliminar(producto)
        else:
            self.carrito[id]["cantidad"] = nueva_cantidad
        self.save()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True