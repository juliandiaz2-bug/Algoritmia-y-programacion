n = int(input("Introduce un número: "))
d = 2

while n > 1:
    if n % d == 0:
        print(d)
        n = n // d
    else:
        d = d + 1