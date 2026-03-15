print("Los valores son:")
for i in range(1, 10):    
    p = 2 ** i     
    if 20 <= p <= 220:  
        print(p, end=" ")
print()

a =int(input("Ingrese el valor inicial:\n"))
b =int(input("Ingrese el valor final:\n"))
q = 0
for i in range(a, b + 1):
    if i % 2 != 0: 
        q =q+ i
print(f"La suma de impares entre {a} y {b} es: {q}",end="")
print()
n = int(input("Ingrese un valor :"))
S = 0
e=n

while n > 0:
    w = n % 10 
    if w % 2 != 0:    
        S = S + w        
    n = n // 10      
print(f"La suma de los dígitos impares de {e} es:{S}", end="")
