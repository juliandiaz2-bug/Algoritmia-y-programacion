def sum(a,b):
    """
    Suma dos números.
    
    Entradas:
        a (numérico): Primer sumando.
        b (numérico): Segundo sumando.
        
    Retorna:
        numérico: La suma de a + b.
    """
    return a + b 
def rest(a,b):
    """Resta dos números."""
    return a-b
def mult(a,b):
    """Multiplica dos números."""
    return a*b
def div ( a,b):
    """Divide dos números."""
    if b == 0:
        return "Error: División por cero"
    return a/b
def raiz_cuadrada(a):
    """Calcula la raíz cuadrada de un número."""
    if a < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return a**0.5
def exponen(a, b):
    """
    Calcula la potencia de una base elevada a un exponente mediante bucles.
    
    Entradas:
        a (numérico): Base de la potencia.
        b (int): Exponente (debe ser entero no negativo).
        
    Retorna:
        numérico/str: Resultado de a^b o mensaje de error según el caso.
    """
    if b < 0:
        return "Error: El exponente no puede ser negativo"
    if a == 0 and b == 0:
        return "Error: 0 elevado a la 0 es indeterminado"
    if a == 0:        return 0
    if b == 0:        return 1
    exponen = 1
    for i in range(1, int(b) + 1): # El rango va desde 1 hasta b (inclusive) para multiplicar a por sí mismo b veces
        exponen *= a
    return exponen

def factorial(n):
    """
    Calcula el producto de todos los enteros positivos desde 1 hasta n.
    
    Entradas:
        n (int): Número para calcular el factorial.
        
    Retorna:
        int/str: El factorial resultante o mensaje de error si n es negativo.
    """
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1): # El rango va desde 2 hasta n (inclusive) para multiplicar todos los números enteros positivos hasta n
        result *= i
    return result
def inverse(a):
    """
    Calcula el inverso multiplicativo (1/a).
    
    Entradas:
        a (numérico): Número a invertir.
        
    Retorna:
        float/str: El valor de 1/a o mensaje de error si a es cero.
    """
    if a == 0:
        return "Error: No se puede calcular el inverso de cero"
    return 1/a
def inverse(b):
    """
    Calcula el inverso multiplicativo (1/b).
    
    Entradas:
        b (numérico): Número a invertir.
        
    Retorna:
        float/str: El valor de 1/b o mensaje de error si b es cero.
    """
    if b == 0:
        return "Error: No se puede calcular el inverso de cero"
    return 1/b

a = float(input("Ingresa un numero: "))
b = float(input("Ingresa otro numero: "))
print(f"Suma: {sum(a, b)}\n")
print(f"Resta: {rest(a, b)}\n")
print(f"Multiplicación: {mult(a, b)}\n")
print(f"División: {div(a, b)}\n")
print(f"Raíz cuadrada de a: {raiz_cuadrada(a)}\n")
print(f"Raíz cuadrada de b: {raiz_cuadrada(b)}\n")
print(f"Exponente a^b: {exponen(a, b)}\n")
print(f"Exponente b^a: {exponen(b, a)}\n")
n = int(input("Ingresa un número para calcular su factorial: "))
print(f"Factorial de {n}: {factorial(n):.2f}")
print(f"Inverso de a: {inverse(a):.2f}")
print(f"Inverso de b: {inverse(b):.2f}")