n = float(input("Ingresa el primer número: "))
x=input("Seleccione la operación a realizar: ")
b=float(input("Ingresa el segundo número: "))
if x=="+":
    print("El resultado de sumar=", n + b )
elif x=="-":
    print("El resultado de restar=", n - b )
elif x=="*":
    print("El resultado de multiplicar=", n * b )
elif x=="/":
    if b != 0: #el != lo que hace es excluir el valor, es decir, si "y" es diferente de 0, entonces se realiza la división
        print("El resultado de dividir=", n / b )
    else:
        print("No es posible la division")