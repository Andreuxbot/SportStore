# test_main.py

import main

def setup_function():
    # Se ejecuta antes de cada test
    main.resetear_productos()

def test_crear_producto_exitoso():
    producto = {
        "id": 1,
        "nombre": "Pelota",
        "descripcion": "Pelota de fútbol talla 5",
        "precio": 120,
        "cantidad": 10
    }
    assert main.crear_producto(producto) is True

def test_crear_producto_duplicado():
    producto = {
        "id": 1,
        "nombre": "Pelota",
        "descripcion": "Pelota de fútbol talla 5",
        "precio": 120,
        "cantidad": 10
    }
    main.crear_producto(producto)
    assert main.crear_producto(producto) is False

def test_leer_producto_existente():
    producto = {
        "id": 2,
        "nombre": "Raqueta",
        "descripcion": "Raqueta de tenis profesional",
        "precio": 300,
        "cantidad": 5
    }
    main.crear_producto(producto)
    resultado = main.leer_producto(2)
    assert resultado is not None
    assert resultado["nombre"] == "Raqueta"

def test_actualizar_producto_existente():
    producto = {
        "id": 3,
        "nombre": "Bicicleta",
        "descripcion": "Bicicleta de montaña",
        "precio": 1500,
        "cantidad": 2
    }
    main.crear_producto(producto)
    assert main.actualizar_producto(3, {"precio": 1400}) is True
    assert main.leer_producto(3)["precio"] == 1400

def test_eliminar_producto_existente():
    producto = {
        "id": 4,
        "nombre": "Guantes",
        "descripcion": "Guantes de boxeo",
        "precio": 100,
        "cantidad": 8
    }
    main.crear_producto(producto)
    assert main.eliminar_producto(4) is True

# ❌ Este test está diseñado para fallar
def test_fallo_intencional():
    producto = {
        "id": 5,
        "nombre": "Balón",
        "descripcion": "Balón de baloncesto",
        "precio": 130,
        "cantidad": 4
    }
    main.crear_producto(producto)
    # Esto fallará porque el precio NO es 0
    assert main.leer_producto(5)["precio"] == 0