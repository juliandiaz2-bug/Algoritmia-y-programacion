def suma_resusevia(lista):
    """Calcula la suma de los elementos en una lista de forma recursiva."""
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

