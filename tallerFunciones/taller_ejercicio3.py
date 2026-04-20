def agregar_producto(diccionario, nombre, cantidad, precio):
    """
    Agrega un nuevo producto al inventario o actualiza sus valores si ya existe.

    Si el producto ya está en el diccionario, suma la nueva cantidad a la existente
    y actualiza el precio. Si no existe, crea una nueva entrada.

    Entradas:
        diccionario (dict): El inventario donde se almacenan los productos.
        nombre (str): El nombre identificador del producto.
        cantidad (int/float): La cantidad de unidades a añadir.
        precio (float): El precio unitario del producto.
    """
    if nombre in diccionario:
        diccionario[nombre]['cantidad'] += cantidad
        diccionario[nombre]['precio'] = precio
    else:
        diccionario[nombre] = {'cantidad': cantidad, 'precio': precio}
def eliminar_producto(diccionario, nombre):
    """
    Elimina un producto específico del inventario por su nombre.

    Entradas:
        diccionario (dict): El inventario del cual se eliminará el producto.
        nombre (str): El nombre del producto que se desea borrar.
    """
    if nombre in diccionario:
        del diccionario[nombre]
def calcular_valor_total(diccionario):
    """
    Calcula el valor monetario total de todos los productos en el inventario.

    Multiplica la cantidad por el precio de cada artículo y suma los resultados.

    Entradas:
        diccionario (dict): El inventario con los datos de productos.

    Retorna:
        float: La suma total del valor (cantidad * precio) de todo el inventario.
    """
    total = 0
    for detalles in diccionario.values():   #.values() devuelve una vista de los valores del diccionario, que en este caso son los detalles de cada producto
        total += detalles['cantidad'] * detalles['precio']
    return total
def mostrar_inventario(diccionario):
    """
    Imprime en pantalla la lista detallada de todos los productos.

    Muestra el nombre, la cantidad disponible y el precio unitario de cada ítem.

    Entradas:
        diccionario (dict): El inventario que se desea visualizar.
    """
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
