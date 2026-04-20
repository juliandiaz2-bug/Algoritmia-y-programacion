from math import prod


def metodo_de_pago(monto, metodo_pago):
    """
    Valida y procesa el método de pago seleccionado por el usuario.

    Entradas:
        monto (float): La cantidad de dinero a pagar.
        metodo_pago (str): El medio elegido (ej. "tarjeta" o "efectivo").

    Retorna:
        float/None: El monto si el método es válido, de lo contrario no retorna nada 
                    e informa el error por consola.
    """
    if metodo_pago == "tarjeta":
        return monto
    elif metodo_pago == "efectivo":
        return monto 
    else:
        print("Método de pago no válido,por favor intente con tarjeta o efectivo.") 

def proceso_de_pago(precio,pago):
    """
    Verifica si el dinero entregado cubre el costo del producto.

    Entradas:
        precio (float): El costo del artículo seleccionado.
        pago (float): La cantidad de dinero ingresada por el usuario.

    Retorna:
        str: "Pago exitoso" si el monto es suficiente, o "Pago insuficiente" en caso contrario.
    """
    if pago >= precio:
        return "Pago exitoso"
    else:
        return "Pago insuficiente"

def productos_de_la_maquina():
    """
    Define el catálogo de productos disponibles en la máquina.

    Contiene un diccionario con el código, nombre y precio de cada artículo.

    Retorna:
        dict: Diccionario anidado con la información de los productos.
    """
    productos = {
        "1": {"nombre": "Coca-Cola", "precio": 3000},
        "2": {"nombre": "Pepsi", "precio": 2500},
        "3": {"nombre": "Agua", "precio": 1700},
        "4": {"nombre": "Jugo", "precio": 2000},
        "5": {"nombre": "Chips", "precio": 3000}
    }
    return productos
def dar_vuelto(monto_pagado, precio):
    """
    Calcula el cambio que debe devolverse al cliente tras una compra.

    Entradas:
        monto_pagado (float): Dinero total entregado por el usuario.
        precio (float): Costo total de la compra.

    Retorna:
        str: Un mensaje indicando el valor del vuelto o que no se requiere.
    """
    if monto_pagado > precio:
        vuelto = monto_pagado - precio
        return f"Su vuelto es: {vuelto} pesos"
    else:
        return "No se requiere dar vuelto"
print("Bienvenido a la máquina expendedora, estos son los productos disponibles:")
for codigo, info in productos_de_la_maquina().items():#codigo es la clave del diccionario (1, 2, 3, etc.) e info es el valor asociado a esa clave (otro diccionario con 'nombre' y 'precio')
    print(f"{codigo}. {info['nombre']} - {info['precio']} pesos")
p=int(input("Ingrese el número del producto que desea comprar: "))
if p < 1 or p > 5:
    print("Producto no válido")
productos = productos_de_la_maquina()
if str(p) in productos:
    precio = productos[str(p)]["precio"]
    nombre_prod = productos[str(p)]["nombre"]
    print(f"El producto {nombre_prod} cuesta: {precio} pesos")
    metodo_pago = input("Ingrese el método de pago (tarjeta/efectivo): ")
    monto_pago = metodo_de_pago(precio, metodo_pago)
    if monto_pago is not None:
        monto_usuario = float(input("Ingrese el monto con el que va a pagar: "))
    resultado_pago = proceso_de_pago(precio, monto_usuario)
    print(resultado_pago)
    if resultado_pago == "Pago exitoso":    
        print(f"Entregando: {nombre_prod}") 
        print(dar_vuelto(monto_usuario, precio)) 
        print("Gracias por su compra, vuelva pronto!")
else:
    print("Producto no encontrado, ingrese un número del 1 al 5")