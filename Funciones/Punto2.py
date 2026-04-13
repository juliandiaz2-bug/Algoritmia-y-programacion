def procesar_lista(lista):
    resultado = []
    for elemento in lista:
        if isinstance(elemento, int):
            resultado.append(elemento * 2)
        elif isinstance(elemento, str):
            resultado.append(elemento.upper())
        else:
            resultado.append(elemento)
    return resultado
K=int(input("Ingrese el número de elementos en la lista: "))
mi_lista = []
for i in range(K):
    r = input(f"Ingrese el elemento {i + 1}: ")
    if r.isdigit():
        m = int(r)
    else:
        m = r
    mi_lista.append(m)
s = procesar_lista(mi_lista)
print("Lista procesada:", s)