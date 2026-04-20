def suma_resusevia(lista):
    """
    Calcula el promedio (media aritmética) de una lista de números.

    Entradas:
        lista (list): Una secuencia de números enteros o flotantes.

    Retorna:
        float: El resultado del promedio. Si la lista está vacía, retorna 0.
    """
    if not lista:
        return 0
    else:
        return lista[0] + suma_resusevia(lista[1:])
K=int(input("Ingrese el número de elementos en la lista: "))
m = []
for i in range(K):  
    n = int(input(f"Ingrese el elemento {i + 1}: "))
    m.append(n)
r = suma_resusevia(m)
print(f"La suma de los elementos en la lista es: {r}")

