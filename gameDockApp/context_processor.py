def total_carrito(request):
    total = 0
    if request.session["carrito"]:
        for key, value in request.session.get("carrito").items():
            total += float(value.get("precio")*value.get("cantidad"))
    return {"total_carrito": total}
