p =input("¿Se ha lanzado el dado? ")
if  p == "si" or p == "Si" or p == "SI" or p == "sI":
    a = int(input("¿Qué número ha salido? "))
    if a == 1:
        print("Posición en x = x + 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif a == 2:
        print("Posición en y = y - 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif a == 3:
        print("Posición en x = x - 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif a == 4:
        print("Posición en y = y + 1")
        print("Actualizando posición de la ficha...")
        print("Vuelve a lanzar el dado")
        print("+1 lanzamiento")
    elif a < 1 or a > 4:
        print("Número inválido, repetir lanzamiento")
elif p == "no" or p == "No" or p == "NO" or p == "nO" :
    print("Esperando lanzamiento del dado...")