def procesar_lista(lista):
    """
    Filtra los números pares de una lista y los eleva al cuadrado usando recursión.

    La función recorre la lista elemento por elemento; si el número es par, 
    lo eleva al cuadrado y lo añade a la lista resultante. Si es impar, 
    lo ignora.

    Entradas:
        lista (list): Una secuencia de números enteros.

    Retorna:
        list: Una nueva lista que contiene solo los cuadrados de los números pares originales.
    """
    if not lista:
        return []
    primero=lista[0]
    resto=procesar_lista(lista[1:])
    if primero % 2 == 0:
        return [primero**2] + resto
    else:
        return resto
    
K=int(input("Ingrese el número de elementos en la lista: "))
m = []
for i in range(K):  
    n = int(input(f"Ingrese el elemento {i + 1}: "))
    m.append(n)

r = procesar_lista(m)
print("Lista procesada (solo números pares):", r)