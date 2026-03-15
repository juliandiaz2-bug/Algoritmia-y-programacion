while True:
    print("Inicio")
    v = input("¿Detector de vacio activado?: ")
    
    if v == "si":
        print("Abrir válvula de entrada")
        l = "no"
        while l == "no":
            l = input("¿Detector de tanque lleno activado? : ")
            
            if l == "no":
                print("Abriendo válvula de entrada") 
            elif l == "si":
                print("Cerrar válvula")
                print("Fin")
                
        break 
        
    elif v == "no":
        
        pass 
        
    elif v == "apagar":
        print("Sistema detenido manualmente")
        break