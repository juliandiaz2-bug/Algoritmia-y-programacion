
def factorial(n):
    """Calcula el factorial de un número."""
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
