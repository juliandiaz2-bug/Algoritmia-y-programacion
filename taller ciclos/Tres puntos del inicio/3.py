i = {"Manzana": 2.5,
    "Banana": 1.8,
    "Naranja": 3.0,
    "Pera": 2.0,
    "Monster": 5.0,
    "Agua": 1.0,
    "Coca-Cola": 3.5}
p = "Manzana"
if p in i:
    print(f"{p} cuesta ${i[p]}")
n = "Uvas"
v = 4.0
i[n] = v
a = "Naranja"
m = 3.2
i[a] = m
e = "Monster"
if e in i:
    i.pop(e)
print(i)