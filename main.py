# main.py

productos = []

def crear_producto(producto):
    for p in productos:
        if p["id"] == producto["id"]:
            return False  # ID duplicado
    productos.append(producto)
    return True

def leer_producto(producto_id):
    for p in productos:
        if p["id"] == producto_id:
            return p
    return None

def actualizar_producto(producto_id, nuevos_datos):
    for p in productos:
        if p["id"] == producto_id:
            p.update(nuevos_datos)
            return True
    return False

def eliminar_producto(producto_id):
    for i, p in enumerate(productos):
        if p["id"] == producto_id:
            del productos[i]
            return True
    return False

def resetear_productos():
    global productos
    productos = []