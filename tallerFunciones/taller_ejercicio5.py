import random

def elegir_semilla():
    """
    Configura la semilla del generador de números aleatorios.
    
    Permite al usuario ingresar una cadena de texto para fijar la secuencia 
    aleatoria (útil para pruebas). Si el usuario presiona Enter sin escribir 
    nada, se mantiene la semilla predeterminada del sistema.

    Entradas:
        Ninguna (Lee desde teclado).
    """
    print("\nseleccion de semilla:")
    print("Selecciona una semilla para generar números aleatorios:")
Semilla_elegida= input("Ingresa el número correspondiente a la semilla o presiona Enter para usar la semilla predeterminada: ")
if Semilla_elegida.strip() != "":  #strip() elimina los espacios en blanco al principio y al final de la cadena, lo que permite verificar si el usuario ingresó algo o dejó el campo vacío.  y != "" es una condición que verifica si la cadena no está vacía. Si el usuario ingresó una semilla válida, se establece esa semilla para el generador de números aleatorios utilizando random.seed(Semilla_elegida). Si el usuario no ingresó una semilla válida (es decir, dejó el campo vacío), se muestra un mensaje indicando que se utilizará la semilla predeterminada.
        random.seed(Semilla_elegida)
else:
        print("No se ingresó una semilla válida. Se utilizará la semilla predeterminada.")

def dificultad():
    """
    Muestra el menú de niveles y gestiona la cantidad de intentos permitidos.
    
    Presenta opciones desde 'Fácil' hasta 'Infernal'. Incluye una opción 
    para salir del programa y una opción oculta (6).

    Entradas:
        Ninguna (Interacción por consola).

    Retorna:
        int: El número de intentos totales asignados a la dificultad elegida.
    """
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil(10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Difícil(4 intentos)")
    print("4. infernal(2 intentos)")
    print("5. salir")
    #print("6.Secreto(1 intento)") 
    while True:
        opcion = input("Ingresa el número correspondiente a la dificultad: ")
        if opcion == "1":
            return 10
        elif opcion == "2":
            return 7
        elif opcion == "3":
            return 4
        elif opcion == "4":
            return 2
        elif opcion == "5":
            print("Saliendo del juego. ¡Hasta luego!")
            exit()
        elif opcion == "6":
            return 1
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 5...?")

def generar_numero():
    """
    Genera un número entero aleatorio entre 1 y 100.

    Entradas:
        Ninguna.

    Retorna:
        int: Un número aleatorio inclusivo entre 1 y 100.
    """
    return random.randint(1, 100) #Genera un número aleatorio entre 1 y 100 (inclusive)
def jugar():
    """
    Ejecuta el bucle principal del juego de adivinanzas.
    
    Coordina la selección de semilla, dificultad y la lógica de intentos. 
    Valida que las entradas del usuario sean números enteros y proporciona 
    pistas de "Demasiado alto" o "Demasiado bajo".

    Entradas:
        Ninguna (Orquestador principal).
    """
    elegir_semilla()
    numero = generar_numero()
    intentos_restantes = dificultad()
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Seras capaz de adivinarlo?")
    while intentos_restantes > 0:
        try:
            intento = int(input("Ingresa tu intento: "))
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
            continue
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.")
        if intentos_restantes == 0:
            print(f"\033[31mLo siento, has agotado tus intentos. El número secreto era {numero}.\033[0m")
            break
        if intento < numero:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"\033[32m¡Felicidades! Has adivinado el número {numero} correctamente.\033[0m")
            break

if __name__ == "__main__":#El bloque if __name__ == "__main__": se utiliza para asegurarse de que el código dentro de este bloque solo se ejecute cuando el script se ejecute directamente, y no cuando se importe como un módulo en otro script. Esto es útil para evitar que el juego se inicie automáticamente si este archivo se importa desde otro lugar. Si el script se ejecuta directamente, se llamará a la función jugar() para iniciar el juego.
    jugar()


    