def agregar_producto(diccionario, nombre, cantidad, precio):
    if nombre in diccionario:
        diccionario[nombre]['cantidad'] += cantidad
        diccionario[nombre]['precio'] = precio
    else:
        diccionario[nombre] = {'cantidad': cantidad, 'precio': precio}
def eliminar_producto(diccionario, nombre):
    if nombre in diccionario:
        del diccionario[nombre]
def calcular_valor_total(diccionario):
    total = 0
    for detalles in diccionario.values():   #.values() devuelve una vista de los valores del diccionario, que en este caso son los detalles de cada producto
        total += detalles['cantidad'] * detalles['precio']
    return total
def mostrar_inventario(diccionario):
    for nombre, detalles in diccionario.items():    #.items() devuelve una vista de los pares clave-valor del diccionario, lo que permite iterar sobre ambos al mismo tiempo                       
        print(f"Producto: {nombre}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
inventario = {}
while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Calcular valor total del inventario")
    print("4. Mostrar inventario")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        agregar_producto(inventario, nombre, cantidad, precio)
    elif opcion == '2':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre)
    elif opcion == '3':
        total = calcular_valor_total(inventario)
        print(f"Valor total del inventario: {total:.2f}")
    elif opcion == '4':
        mostrar_inventario(inventario)
    elif opcion == '5':
        break
    else:
        print("Por Dios te di 5 opciones, elige una de esas, no seas tonto")
