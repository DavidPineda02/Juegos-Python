import random

# Dibujos del ahorcado en diferentes estados
ahorcado01 = ('''
                   +----+
                  ''')

ahorcado02 = ('''
                   +----+
                   |
                   ''')

ahorcado03 = ('''
                   +----+
                   |    |
                        |
                        |
                        |
                        |
                        |
                   ''')

ahorcado04 = ('''
                   +----+
                   |    |
                        |
                        |
                        |
                        |
                        |
                   ========
                   ''')

ahorcado05 = ('''
                   +----+
                   |    |
                   O    |
                        |
                        |
                        |
                        |
                   ========
                   ''')

ahorcado06 = ('''
                   +----+
                   |    |
                   O    |
                   |    |
                        |
                        |
                        |
                   ========
                   ''')

ahorcado07 = ('''
                   +----+
                   |    |
                   O    |
                  /|    |
                        |
                        |
                        |
                   ========
                   ''')

ahorcado08 = ('''
                   +----+
                   |    |
                   O    |
                  /|\   |
                        |
                        |
                        |
                   ========
                   ''')

ahorcado09 = ('''
                   +----+
                   |    |
                   O    |
                  /|\   |
                  /     |
                        |
                        |
                   ========
                   ''')

ahorcado10 = ('''
                   ¡Perdiste!

                   +----+
                   |    |
                   O    |
                  /|\   |
                  / \   |
                        |
                        |
                   ========
                   ''')

# Variables globales
letrasAdivinadas = []  # Lista para almacenar las letras adivinadas
letrasDescartadas = []  # Lista para almacenar las letras incorrectas
listaAbecedario = list("a b c d e f g h i j k l m n ñ o p q r s t u v w x y z")  # Abecedario válido
diccionarioPalabras = {}  # Diccionario para almacenar las palabras agregadas
intentosMax = 10  # Número máximo de intentos permitidos


def agregar():
    """
    Permite al usuario agregar palabras al diccionario.
    """
    cantPalabras = int(input("\nCuántas palabras desea agregar? "))  # Solicita la cantidad de palabras a agregar
    for word in range(cantPalabras):  # Itera según la cantidad de palabras ingresada
        palabra = input(f"Ingrese la palabra {word+1}: ").lower().strip()  # Solicita la palabra y la normaliza
        diccionarioPalabras[word+1] = palabra  # Almacena la palabra en el diccionario con una clave numérica


def configurar():
    """
    Configura el número máximo de errores permitidos.
    Retorna:
        int: Número de intentos máximos configurados.
    """
    global intentosMax  # Usa la variable global para modificarla
    equivocarse = int(input("\nCuántas veces puede equivocarse? (Máximo : 10) "))  # Solicita el número de intentos
    if 1 <= equivocarse <= 10:  # Verifica que el número esté dentro del rango permitido
        intentosMax = equivocarse  # Actualiza el número máximo de intentos
    else:
        print("Valor no permitido. Se mantiene en 10 Intentos.")  # Mensaje si el valor no es válido
        intentosMax = 10  # Restaura el valor predeterminado

    return intentosMax  # Retorna el número de intentos máximo configurado


def palabra_secreta(diccionarioPalabras):
    """
    Selecciona una palabra secreta aleatoria del diccionario.
    Parámetros:
        diccionarioPalabras (dict): Diccionario con las palabras disponibles.
    Retorna:
        str: Palabra secreta seleccionada.
    """
    opciones = list(diccionarioPalabras.values())  # Extrae las palabras del diccionario como una lista
    palabraSecreta = random.choice(opciones)  # Elige una palabra al azar de la lista
    return palabraSecreta  # Retorna la palabra secreta seleccionada


def jugar():
    """
    Ejecuta el juego del ahorcado.
    """
    global intentosMax  # Usa la variable global para acceder al número de intentos

    # Verifica si hay palabras disponibles para jugar
    if len(diccionarioPalabras) == 0:  # Si el diccionario está vacío
        print("No hay palabras para jugar.")  # Muestra un mensaje de error
        return  # Sale de la función

    palabra = palabra_secreta(diccionarioPalabras)  # Selecciona una palabra secreta
    errores = 0  # Inicializa el contador de errores
    progresoLetras = ["_" for _ in palabra]  # Crea una lista con guiones bajos para representar la palabra
    letrasAdivinadas.clear()  # Limpia la lista de letras adivinadas
    letrasDescartadas.clear()  # Limpia la lista de letras descartadas

    # Bucle principal del juego
    while errores < intentosMax and "_" in progresoLetras:  # Continúa mientras haya intentos y letras por adivinar
        print(" ".join(progresoLetras))  # Muestra el progreso actual de la palabra
        letra = input("\nAdivina una letra: ").lower().strip()  # Solicita una letra al usuario y la normaliza
        print(f"\nLetras descartadas: {' '.join(letrasDescartadas)}\n")  # Muestra las letras descartadas

        # Validación de la entrada
        if letra == palabra:  # Si el usuario adivina la palabra completa
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")  # Muestra un mensaje de éxito
            return  # Termina el juego

        if len(letra) != 1 or letra not in listaAbecedario:  # Verifica que sea una letra válida
            print("\nPor favor, ingresa una letra válida.")  # Muestra un mensaje de error
            continue  # Vuelve al inicio del bucle

        if letra in letrasAdivinadas or letra in letrasDescartadas:  # Verifica que la letra no se haya usado antes
            print("Ya usaste esa letra. Intenta otra.")  # Muestra un mensaje de advertencia
            continue  # Vuelve al inicio del bucle

        # Procesamiento de la letra ingresada
        if letra in palabra:  # Si la letra está en la palabra
            letrasAdivinadas.append(letra)  # Agrega la letra a las adivinadas
            for i, l in enumerate(palabra):  # Recorre la palabra para actualizar el progreso
                if l == letra:  # Si la letra coincide con una letra de la palabra
                    progresoLetras[i] = letra  # Actualiza el progreso con la letra adivinada
            print("¡Correcto!\n")  # Muestra un mensaje de éxito
        else:  # Si la letra no está en la palabra
            letrasDescartadas.append(letra)  # Agrega la letra a las descartadas
            errores += 1  # Incrementa el contador de errores
            print("¡Incorrecto!")  # Muestra un mensaje de error

        # Muestra el dibujo correspondiente al número de errores
        if errores == 1:
            print(ahorcado01)
        elif errores == 2:
            print(ahorcado02)
        elif errores == 3:
            print(ahorcado03)
        elif errores == 4:
            print(ahorcado04)
        elif errores == 5:
            print(ahorcado05)
        elif errores == 6:
            print(ahorcado06)
        elif errores == 7:
            print(ahorcado07)
        elif errores == 8:
            print(ahorcado08)
        elif errores == 9:
            print(ahorcado09)

    # Resultado final del juego
    if "_" not in progresoLetras:  # Si el usuario adivinó todas las letras
        print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}\n")  # Muestra un mensaje de éxito
    else:  # Si el usuario agotó los intentos
        print(ahorcado10)
        print(f"\nLo siento, perdiste. La palabra era: {palabra}\n")  # Muestra un mensaje de derrota


# Menú principal del juego
while True:
    print("\n======= Juego Del Ahorcado =======")
    print("\n1. Agregar Palabras.  \n2. Configurar. \n3. Jugar. \n4. Salir.")

    seleccion = int(input("\nSeleccione una opción (1-4): "))  # Solicita la opción del menú

    if seleccion not in range(1, 5):  # Verifica que la opción sea válida
        print("\nOpción no válida. Intente de nuevo (1-4).")  # Muestra un mensaje de error
        continue  # Vuelve al inicio del bucle

    if seleccion == 1:  # Agregar palabras
        agregar()
        print("\n------ Lista de Palabras ------ ")
        for i, palabras in diccionarioPalabras.items():  # Muestra las palabras agregadas
            print(i, palabras)
        continue

    elif seleccion == 2:  # Configurar intentos máximos
        configurar()
        continue

    elif seleccion == 3:  # Jugar
        print("Comenzando el juego...\n")
        jugar()
        continue

    elif seleccion == 4:  # Salir
        print("\nGracias por jugar.")
        print("\n==================================")
        break