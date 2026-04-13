def procesar_lista(lista):
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