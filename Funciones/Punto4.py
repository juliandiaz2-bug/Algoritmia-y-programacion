def invertir_cadena(cadena):
    """
    Invierte el orden de los caracteres de un texto usando recursión.

    Toma el último carácter de la cadena y lo concatena con el resultado 
    de invertir el resto de la cadena (desde el principio hasta el penúltimo).

    Entradas:
        cadena (str): El texto que se desea invertir.

    Retorna:
        str: La cadena de texto invertida. Retorna un string vacío si la entrada está vacía.
    """
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
k= input("Ingrese una cadena para invertir: ")
r = invertir_cadena(k)
print("Cadena invertida:", r)