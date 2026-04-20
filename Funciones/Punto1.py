
def factorial(n):
    """
    Calcula el producto de todos los números enteros positivos desde 1 hasta n.

    Utiliza un enfoque iterativo (bucle for) para obtener el resultado. 
    Maneja casos especiales para 0, 1 y números negativos.

    Entradas:
        n (int): El número entero del cual se desea obtener el factorial.

    Retorna:
        int/str: El valor del factorial si n >= 0, o un mensaje de error 
                 si el número ingresado es negativo.
    """
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n=int(input("Ingrese un número para calcular su factorial: "))
if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {n} es: {factorial(n)}")
