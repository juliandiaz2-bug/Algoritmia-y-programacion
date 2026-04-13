def suma_resusevia(a, b):
    if b == 0:
        return a
    else:
        return suma_resusevia(a + 1, b - 1)
k= int(input("Ingrese el primer número: "))
s= int(input("Ingrese el segundo número: "))
resultado = suma_resusevia(k, s)
print(f"La suma de {k} y {s} es: {resultado}")