def invertir_cadena(cadena):
    """Invierte una cadena de texto utilizando recursión."""
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
k= input("Ingrese una cadena para invertir: ")
r = invertir_cadena(k)
print("Cadena invertida:", r)