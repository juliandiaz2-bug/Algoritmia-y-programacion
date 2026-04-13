def encontrar_maximo(lista):
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        maximo_restante = encontrar_maximo(lista[1:])
        return lista[0] if lista[0] > maximo_restante else maximo_restante
K=int(input("Ingrese el número de elementos en la lista: "))
mi_lista = []
for i in range(K):
    n = int(input(f"Ingrese el elemento {i + 1}: "))
    mi_lista.append(n)
s = encontrar_maximo(mi_lista)
if resultado is not None:
    print("El número máximo en la lista es:", resultado)
else:
    print("La lista está vacía, no se puede encontrar un máximo.") 