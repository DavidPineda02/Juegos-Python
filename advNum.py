import random, time

def dificultadJuego():
    # Permite al usuario seleccionar el nivel de dificultad del juego.
    # Retorna:
    #     tuple: Un rango de números (mínimo y máximo) y el número máximo de intentos permitidos.

    print("\nSeleccione el Nivel de Dificultad:")
    print("\n1. Facil (1-50, 10 intentos) \n2. Medio (1-100, 7 intentos) \n3. Dificil (1-200, 5 intentos)")

    while True:  # Bucle para validar la opción ingresada
        opcion = int(input("\nElige la Dificultad (1-2-3): "))
        if opcion == 1:
            return 1, 50, 10  # Rango 1-50, 10 intentos
        elif opcion == 2:
            return 1, 100, 7  # Rango 1-100, 7 intentos
        elif opcion == 3:
            return 1, 200, 5  # Rango 1-200, 5 intentos
        else:
            print("Elige una Opcion Valida.")  # Mensaje de error si la opción no es válida


def numeroRandomico(numMin, numMax):
    # Genera un número aleatorio dentro del rango especificado.
    # Parámetros:
    #     numMin (int): Límite inferior del rango.
    #     numMax (int): Límite superior del rango.
    # Retorna:
    #     int: Número aleatorio generado.

    return random.randint(numMin, numMax)


def pistas(numRandm):
    # Proporciona pistas sobre el número a adivinar.
    # Parámetros:
    #     numRandm (int): Número aleatorio generado.

    if numRandm % 2 == 0:  # Verifica si el número es par
        print("Pista: El Numero es Par.")
    else:
        print("Pista: El Numero es Impar.")

    if numRandm % 5 == 0:  # Verifica si el número es múltiplo de 5
        print("Pista: El Numero es Multiplo de 5.")
    if numRandm % 10 == 0:  # Verifica si el número es múltiplo de 10
        print("Pista: El Numero es Multiplo de 10.")


def validarEntrada(numMin, numMax):
    # Solicita y valida la entrada del usuario dentro del rango especificado.
    # Parámetros:
    #     numMin (int): Límite inferior del rango.
    #     numMax (int): Límite superior del rango.
    # Retorna:
    #     int: Número ingresado por el usuario.

    while True:  # Bucle para validar la entrada
        numUser = int(input(f"\nAdivina el Numero (entre {numMin} y {numMax}): "))
        if numMin <= numUser <= numMax:  # Verifica que el número esté dentro del rango
            return numUser
        else:
            print(f"\nDigita un Numero entre {numMin} y {numMax}.")  # Mensaje de error si el número está fuera del rango


# Programa principal
print("========== Adivina el Numero ==========")

# Selecciona la dificultad y obtiene los parámetros del juego
numMin, numMax, maxIntents = dificultadJuego()
numRandm = numeroRandomico(numMin, numMax)  # Genera el número aleatorio

print(f"\nVoy a Pensar un Numero entre {numMin} y {numMax}. Tienes {maxIntents} intentos.\n")
time.sleep(2)  # Simula un breve retraso mientras "piensa" el número

pistas(numRandm)  # Muestra pistas sobre el número

intentos = 0  # Contador de intentos
tiempoStart = time.time()  # Tiempo de inicio del juego
ganar = False  # Variable para determinar si el jugador ha ganado

while intentos < maxIntents:  # Bucle principal del juego
    numUser = validarEntrada(numMin, numMax)  # Solicita y valida la entrada del usuario
    intentos += 1  # Incrementa el contador de intentos

    if numUser < numRandm:  # Si el número ingresado es menor
        print("\nEl Numero a Adivinar es Mayor. Intenta Nuevamente.")
    elif numUser > numRandm:  # Si el número ingresado es mayor
        print("\nEl Numero a Adivinar es Menor. Intenta Nuevamente.")
    else:  # Si el número ingresado es correcto
        tiempoTranscrr = round(time.time() - tiempoStart, 2)  # Calcula el tiempo transcurrido
        print(f"\nGanaste! Adivinaste el Numero en {intentos} intentos y en {tiempoTranscrr} Segundos.")
        print("\n=======================================")
        ganar = True  # Actualiza la variable
        break  # Sale del bucle

if not ganar:  # Si el jugador no adivinó el número
    tiempoTranscrr = round(time.time() - tiempoStart, 2)  # Calcula el tiempo transcurrido
    print(f"\nPerdiste, Has Agotado tus {maxIntents} intentos. El Numero era {numRandm}.")
    print(f"Tiempo Total Jugado: {tiempoTranscrr} Segundos.")
    print("\n=======================================")