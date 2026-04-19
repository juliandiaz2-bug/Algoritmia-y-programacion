def metodo_de_pago(monto, metodo_pago):
    if metodo_pago == "tarjeta":
        return monto
    elif metodo_pago == "efectivo":
        return monto 
    else:
        print("Método de pago no válido") 

def proceso_de_pago(precio,pago):
    if pago >= precio:
        return "Pago exitoso"
    else:
        return "Pago insuficiente"

def productos_de_la_maquina():
    productos = {
        "1": {"nombre": "Coca-Cola", "precio": 3000},
        "2": {"nombre": "Pepsi", "precio": 2500},
        "3": {"nombre": "Agua", "precio": 1700},
        "4": {"nombre": "Jugo", "precio": 2000},
        "5": {"nombre": "Chips", "precio": 3000}
    }
    return productos
def dar_vuelto(monto_pagado, precio):
    if monto_pagado > precio:
        vuelto = monto_pagado - precio
        return f"Su vuelto es: {vuelto} pesos"
    else:
        return "No se requiere dar vuelto"

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