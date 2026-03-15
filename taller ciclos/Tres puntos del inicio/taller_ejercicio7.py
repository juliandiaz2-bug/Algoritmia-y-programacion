import random

x = 0  
y = 0  
p = 0  

print("El borracho comienza en (0, 0)")
while p < 100:
    d = random.randint(1, 4) 
    
    if d == 1:
        y = y + 1 
    elif d == 2:
        y = y - 1 
    elif d == 3:
        x = x + 1  
    elif d == 4:
        x = x - 1  
        
    p = p + 1  


print("Ubicación final después de 100 pasos: (", x, ",", y, ")")