def generar_numeros_aleatorios(limite_max=100):
    """Genera una lista de números aleatorios dentro de un rango especificado."""
    semilla=id(object)  #id(object) devuelve un número único para el objeto dado, que se puede usar como semilla para generar números aleatorios
    a=1664525
    c=1013904223
    m=2**32
    numeros_aleatorios = []
    for _ in range(10):  # Genera 10 números aleatorios
        p = (a * semilla + c) % m
        numeros_aleatorios.append(p % limite_max)#.append() agrega un elemento a la lista, % limite_max asegura que el número generado esté dentro del rango especificado por el usuario
        semilla = p  # Actualiza la semilla para el siguiente número aleatorio
    return tuple(numeros_aleatorios)  # Devuelve una tupla con los números aleatorios dentro del límite
def elegir_dificultad():
    """Permite al usuario elegir la dificultad del juego."""
    while True:
        if dificultad in ['fácil', 'facil', 'medio', 'difícil', 'dificil', 'infernal']:
            return dificultad.lower()
        else:
            print("Opción no válida. Por favor, elige entre fácil, medio o difícil.")
def intentos_para_dificultad(dificultad):
    """Devuelve el número de intentos permitidos según la dificultad elegida."""
    if dificultad.lower() == 'fácil':
        return 10
    elif dificultad.lower() == 'medio':
        return 7
    elif dificultad.lower() == 'difícil':
        return 5
    elif dificultad.lower() == 'infernal':
        return 3
def normalizar_dificultad(dificultad):
    """Normaliza la entrada de dificultad para manejar diferentes formas de escribirla."""
    if dificultad.lower() in ['fácil', 'facil']:
        return 'fácil'
    elif dificultad.lower() == 'medio':
        return 'medio'
    elif dificultad.lower() in ['difícil', 'dificil']:
        return 'difícil'
    elif dificultad.lower() == 'infernal':
        return 'infernal'
    else:
        return None
def jugar_segun_intentos(intentos, numeros_aleatorios):
    """Permite al usuario jugar el juego de adivinar números según los intentos permitidos."""
    print(f"Tienes {intentos} intentos para adivinar los números.")
    for intento in range(1, intentos + 1):
        try:
            adivinanza = int(input(f"Intento {intento}: Ingresa un número entre 0 y 99: "))
            if adivinanza in numeros_aleatorios:
                print("¡Felicidades! Has adivinado un número.")
                return True
            else:
                print("Número incorrecto. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
    print("Lo siento, has agotado tus intentos. Los números eran:", numeros_aleatorios)
    return False
numeros_aleatorios = generar_numeros_aleatorios()
dificultad = elegir_dificultad()
intentos = intentos_para_dificultad(dificultad)
jugar_segun_intentos(intentos, numeros_aleatorios)

i=int(input("Ingresa un número entre 0 y 100: "))
if i in generar_numeros_aleatorios():
    print("¡Felicidades! Has adivinado un número.")
else:
    print("Número incorrecto. Intenta de nuevo.")
