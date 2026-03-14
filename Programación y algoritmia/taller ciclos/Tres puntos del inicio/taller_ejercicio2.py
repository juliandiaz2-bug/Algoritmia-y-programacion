s=0
for x in range(1,101,2):
 s=s + x
print(f"La suma de los pares es: {s}\n")

m=0
for p in range(1,100):
 m=m + (p**2)
print(f"La suma de los cuadrados es: {m}\n")

a =int(input("Ingrese el valor inicial:\n"))
b =int(input("Ingrese el valor final:\n"))
q = 0
for i in range(a, b + 1):
    if i % 2 != 0: 
        q =q+ i
print(f"La suma de impares entre {a} y {b} es: {q}")

n = int(input("Ingrese un valor :"))
S = 0
e=n

while n > 0:
    w = n % 10 
    if w % 2 != 0:    
        S = S + w        
    n = n // 10      
print(f"La suma de los dígitos impares de {e} es:{S}")