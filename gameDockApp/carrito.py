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
            for key, value in self.carrito.keys():
                if key == str(id):
                    value["cantidad"] += 1
                    break
        self.save()


    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True


    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.save()


    def decrementar(self, producto):
        id = str(producto.id)
        for key, value in self.carrito.keys():
            if key == id:
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")
        self.save()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True