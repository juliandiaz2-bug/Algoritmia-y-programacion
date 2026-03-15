n = int(input("Ingrese el valor de n:\n "))
x =0
print("cuadrados")
while x * x < n:
    print( x * x,end=" ") 
    x =x + 1
print()
k = 10
print("Divisibles por 10:")
while k < n:
    print(k,end=" " )
    k =k + 10
print()
c = 0
print("Potencias de 2:")
while 2 ** c < n:
    print(2 ** c,end=" ")
    c =c + 1
