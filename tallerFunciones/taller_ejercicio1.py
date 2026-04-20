
def promedio(lista):
    """
    Calcula la media aritmética de una lista de números.

    entradas:
        lista (list[float/int]): Una secuencia de números.

    Returns:
        float: El promedio de los elementos. Retorna 0 si la lista está vacía
        para evitar errores de división por cero.
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def extremos(lista):
    """
    Determina los valores mínimo y máximo de una lista.

    Entradas:
        lista (list): Una secuencia de números.

    Retorna:
        tuple: Una tupla con (mínimo, máximo). Devuelve (None, None) si está vacía.
    """
    if len(lista) == 0:
        return None, None
    return min(lista), max(lista)
def dias_sobre_promedio(lista):
    """
    Cuenta cuántos valores son mayores al promedio de la lista.

    Entradas:
        lista (list): Una secuencia de valores numéricos.

    Retorna:
        int: Número de elementos que superan la media.
    """
    if len(lista) == 0:
        return 0
    prom = promedio(lista)
    return sum(1 for x in lista if x > prom)
 
tem = [float(x) for x in input("Ingresa las temperaturas diarias en celsius separadas por comas: ").split(",")]
print(f"Promedio de temperaturas: {promedio(tem):.2f} celsius")
print(f"Temperatura mínima: {extremos(tem)[0]:.2f} celsius")
print(f"Temperatura máxima: {extremos(tem)[1]:.2f} celsius")
print(f"días con temperatura sobre el promedio: {dias_sobre_promedio(tem)}")