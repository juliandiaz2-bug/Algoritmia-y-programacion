def promedio(lista):
    """Calcula el promedio de una lista de números."""
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def extremos(lista):
    """Devuelve el valor mínimo y máximo de una lista de números."""
    if len(lista) == 0:
        return None, None
    return min(lista), max(lista)
def dias_sobre_promedio(lista):
"""Cuenta cuántos elementos de la lista son mayores que el promedio."""
    if len(lista) == 0:
        return 0
    prom = promedio(lista)
    return sum(1 for x in lista if x > prom)
 
tem = [float(x) for x in input("Ingresa las temperaturas diarias en celsius separadas por comas: ").split(",")]
print(f"Promedio de temperaturas: {promedio(tem):.2f} celsius")
print(f"Temperatura mínima: {extremos(tem)[0]:.2f} celsius")
print(f"Temperatura máxima: {extremos(tem)[1]:.2f} celsius")
print(f"días con temperatura sobre el promedio: {dias_sobre_promedio(tem)}")