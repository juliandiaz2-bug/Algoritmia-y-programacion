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