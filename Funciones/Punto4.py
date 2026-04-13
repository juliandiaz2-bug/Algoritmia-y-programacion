def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
k= input("Ingrese una cadena para invertir: ")
resultado = invertir_cadena(k)
print("Cadena invertida:", resultado)

