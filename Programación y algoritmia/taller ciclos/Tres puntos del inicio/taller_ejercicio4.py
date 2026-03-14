while True:
    print("Registrando hora")
    x = input("¿Son las 6 A.M.? ")
    
    if x == "si":
        print("Sonando alarma")
        a = 0
        while a < 60:
            o = input("¿Se ha apagado la alarma? ")
            if o == "no":
                a = a + 1
                if a != 60:
                    print("Sigue sonando la alarma")
                else:
                    print("apagando alarma")
            elif o == "si":
                print("apagando la alarma")
                a = 60 
                
    elif x == "apagar":
        print("Alarma apagada")
        break 