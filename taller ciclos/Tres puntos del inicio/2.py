a={"juan","luis","esteban","sebastian","manuel"}
b={"juan" : 20,
   "luis" : 30 ,
   "esteban" : 10,
   "sebastian" : 50,
   "manuel" :100}
w=float(0.15)
x=input("¿cual es el cliente?")
if x in a:
    print("su valor a pagar es:", b[x] * w )
else:
    print("Cliente no registrado")
