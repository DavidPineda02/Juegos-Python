# Importamos el módulo random para poder seleccionar preguntas de forma aleatoria
import random

# Diccionario principal que contiene todas las preguntas organizadas por temas
preguntasTrivia = {
    "Arte": [
        {
            "pregunta": "Quien pinto La Mona Lisa?",
            "opciones": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"],
            "respuesta": "Leonardo da Vinci"
        },
        {
            "pregunta": "Cual es el nombre del famoso cuadro de Edvard Munch que representa una figura angustiada en un paisaje distorsionado?",
            "respuesta": "El grito"
        },
        {
            "pregunta": "Cual de estos movimientos artisticos se caracteriza por fragmentar la realidad en formas geometricas?",
            "opciones": ["Cubismo", "Impresionismo", "Surrealismo"],
            "respuesta": "Cubismo"
        }
    ],
    "Ciencia": [
        {
            "pregunta": "Que elemento quimico tiene el simbolo 'O' en la tabla periodica?",
            "respuesta": "Oxigeno"
        },
        {
            "pregunta": "Que organo del cuerpo humano produce la insulina?",
            "opciones": ["Corazon", "Pancreas", "Higado"],
            "respuesta": "Pancreas"
        },
        {
            "pregunta": "Cual es la unidad basica de la vida?",
            "opciones": ["Tejido", "Organo", "Celula"],
            "respuesta": "Celula"
        }
    ],
    "Deporte": [
        {
            "pregunta": "En que deporte se utiliza una red, raqueta con malla y pelota verde?",
            "respuesta": "Tenis"
        },
        {
            "pregunta": "Cuántos jugadores hay en un equipo de futbol en el campo?",
            "opciones": ["9", "10", "11"],
            "respuesta": "11"
        },
        {
            "pregunta": "Que pais ha ganado mas Copas Mundiales de Futbol?",
            "respuesta": "Brasil"
        }
    ],
    "Geografia": [
        {
            "pregunta": "Cual es la capital de Colombia?",
            "opciones": ["Bogota", "Buenos Aires", "Santiago"],
            "respuesta": "Bogota"
        },
        {
            "pregunta": "Cual es el pais mas grande del mundo en extension territorial?",
            "respuesta": "Rusia"
        },
        {
            "pregunta": "Cual es el rio mas largo del mundo?",
            "opciones": ["Nilo", "Amazonas", "Yangtse"],
            "respuesta": "Amazonas"
        }
    ],
    "Entretenimiento": [
        {
            "pregunta": "Que actor interpreto a Iron Man en el cine?",
            "respuesta": "Robert Downey"
        },
        {
            "pregunta": "Cual es el nombre del mago protagonista de Harry Potter?",
            "opciones": ["Harry Potter", "Ron Weasley", "Draco Malfoy"],
            "respuesta": "Harry Potter"
        },
        {
            "pregunta": "Cual es el nombre del actor que interpreta a Jack Sparrow en 'Piratas del Caribe'?",
            "opciones": ["Orlando Bloom", "Geoffrey Rush", "Johnny Depp"],
            "respuesta": "Johnny Depp"
        }
    ],
    "Historia": [
        {
            "pregunta": "En que año llego el hombre a la luna?",
            "opciones": ["1969", "1965", "1972"],
            "respuesta": "1969"
        },
        {
            "pregunta": "En que año comenzo la Segunda Guerra Mundial?",
            "respuesta": "1939"
        },
        {
            "pregunta": "Que civilizacion construyo las piramides de Egipto?",
            "opciones": ["Griega", "Egipcia", "Romana"],
            "respuesta": "Egipcia"
        }
    ]
}

# Creamos una lista vacía donde guardaremos todas las preguntas junto con su tema
preguntasDisponibles = []

# Recorremos cada tema y sus preguntas dentro del diccionario principal
for tema, preguntas in preguntasTrivia.items():
    # Por cada pregunta dentro del tema actual...
    for pregunta in preguntas:
        # ...agregamos el nombre del tema como un campo adicional a la pregunta
        pregunta["tema"] = tema
        # Y añadimos esa pregunta a la lista general de preguntas disponibles
        preguntasDisponibles.append(pregunta)

# Mezclamos aleatoriamente las preguntas para que no salgan siempre en el mismo orden
random.shuffle(preguntasDisponibles)


def mostrarPregunta(pregunta):
    """
    Muestra la pregunta al jugador y recoge su respuesta.
    
    Si la pregunta tiene opciones múltiples, se le permite elegir una por número.
    Si no, se espera una respuesta abierta (texto).
    
    Parámetro:
        pregunta (dict): Diccionario que contiene la pregunta, posibles opciones y la respuesta correcta.
        
    Retorna:
        str o int: Devuelve la opción seleccionada o 0 si el jugador quiere salir.
    """
    # Imprimimos la pregunta
    print(f"\n{pregunta['pregunta']}")
    
    # Si la pregunta tiene opciones múltiples...
    if "opciones" in pregunta:
        print("\nOpciones:")
        # Enumeramos las opciones comenzando desde 1 para facilitar la selección
        for idx, opcion in enumerate(pregunta["opciones"], start=1):
            print(f"{idx}. {opcion}")

        while True:
            # Pedimos al usuario que ingrese el número de la opción que cree correcta
            rta = input("Ingresa el número de la opción (0 para Salir): ")
            
            # Si elige 0, retorna 0 para salir del juego
            if rta == "0":
                return 0
            
            # Si lo ingresado es un número y está dentro del rango válido...
            elif rta.isdigit() and 1 <= int(rta) <= len(pregunta["opciones"]):
                # Retornamos la opción seleccionada (en mayúscula inicial)
                return pregunta["opciones"][int(rta) - 1].capitalize().strip()
            
            else:
                # Si la entrada no es válida, mostramos mensaje de error
                print("Opcion no valida. Inténtalo de nuevo.")
    
    else:
        # Si no hay opciones, pedimos una respuesta directa del usuario
        rta = input("Tu respuesta: ").capitalize().strip()
        return rta


def jugarTrivia():
    """
    Función principal del juego.
    Controla el bucle del juego, muestra preguntas, verifica respuestas,
    lleva puntaje y otorga insignias por temas completados.
    """
    # Mensaje de bienvenida
    print("========== Juego de Trivia (Preguntados) ==========")
    print("\nResponde correctamente a las preguntas de distintos temas para ganar puntos e insignias.")
    print("Presiona 0 en cualquier momento para salir.\n")
    
    # Inicializamos el puntaje del jugador
    puntaje = 0
    
    # Calculamos cuántas preguntas hay en total
    totalPreguntas = len(preguntasDisponibles)

    # Creamos un diccionario para contar aciertos por tema
    # Crea un diccionario donde cada clave es un tema (como "Arte", "Ciencia", etc.) y su valor inicial es 0. Este diccionario servirá para contar cuántas preguntas acertó el jugador en cada tema .
    contadorTemas = {tema: 0 for tema in preguntasTrivia.keys()}
    
    # Iteramos sobre cada pregunta disponible
    for i, pregunta in enumerate(preguntasDisponibles, start=1):
        print(f"\n----- Pregunta {i} de {totalPreguntas} -----")
        print(f"Tema: {pregunta['tema']}")  # Mostramos el tema de la pregunta actual
        
        # Llamamos a la función que muestra la pregunta y devuelve la respuesta del usuario
        rtaUsuario = mostrarPregunta(pregunta)
        
        # Si el usuario responde '0', se sale del juego
        if rtaUsuario == 0 or rtaUsuario == "0":
            print("\nHas decidido salir del juego. ¡Hasta luego!")
            break
        
        # Convertimos la respuesta correcta a formato capitalizado
        rtaCorrecta = pregunta["respuesta"].capitalize().strip()

        # Comparamos la respuesta del usuario con la correcta
        if rtaUsuario == rtaCorrecta:
            print("¡Respuesta Correcta! +1 punto.")
            puntaje += 1  # Sumamos un punto al puntaje total
            contadorTemas[pregunta["tema"]] += 1  # Sumamos un acierto al tema correspondiente
        else:
            # Si falla, mostramos la respuesta correcta
            print(f"Respuesta Incorrecta. La respuesta correcta era: {rtaCorrecta}.")

    # Calculamos las insignias ganadas: deben haberse acertado las 3 preguntas de un tema
    # Estamos creando una lista con los temas en los que el jugador respondió las 3 preguntas correctamente , o sea, aquellos en los que el count es igual a 3.
    insigniasGanadas = [tema for tema, count in contadorTemas.items() if count == 3]
    
    # Mostramos los resultados finales
    print("\n====================")
    print("Juego Terminado!")
    print(f"Puntuación Final: {puntaje}/{totalPreguntas}")
    print(f"Insignias Ganadas ({len(insigniasGanadas)}):")

    if insigniasGanadas:
        # Si hay insignias ganadas, las listamos
        for insignia in insigniasGanadas:
            print(f"🏅 {insignia}")
    else:
        # Si no, informamos que aún no ha ganado ninguna
        print("Aun no has ganado ninguna insignia.")
    
    print("====================")


# Ejecutamos el juego
jugarTrivia()


# import random

# preguntasTrivia = [
#     {
#         "pregunta": "Cual es la capital de Colombia?",
#         "respuesta": "Bogota"
#     },
#     {
#         "pregunta": "En que año comenzo la Segunda Guerra Mundial?",
#         "respuesta": "1939"
#     },
#     {
#         "pregunta": "Cual es el rio mas largo del mundo?",
#         "opciones": ["Nilo", "Amazonas", "Yangtse"],
#         "respuesta": "Amazonas"
#     },
#     {
#         "pregunta": "Quien pinto La Mona Lisa?",
#         "respuesta": "Leonardo da Vinci"
#     },
#     {
#         "pregunta": "Cual es el planeta mas grande del sistema solar?",
#         "respuesta": "Jupiter"
#     },
#     {
#         "pregunta": "Cual es el oceano mas grande del mundo?",
#         "respuesta": "Pacifico"
#     },
#     {
#         "pregunta": "Que elemento quimico tiene el simbolo 'O' en la tabla periodica?",
#         "respuesta": "Oxigeno"
#     },
#     {
#         "pregunta": "En que pais se encuentra la Torre Eiffel?",
#         "opciones": ["Espana", "Francia", "Italia"],
#         "respuesta": "Francia"
#     },
#     {
#         "pregunta": "Cuantos lados tiene un hexagono?",
#         "respuesta": "6"
#     },
#     {
#         "pregunta": "Cual es el autor de la novela 'Cien años de soledad'?",
#         "respuesta": "Gabriel Garcia Marquez"
#     }
# ]

# def mostrarPregunta(pregunta):
#     """
#     Muestra una pregunta al usuario y solicita su respuesta.
    
#     Parámetros:
#         pregunta (dict): Diccionario que contiene la pregunta y la respuesta correcta.
    
#     Retorna:
#         str: Respuesta ingresada por el usuario.
#     """
#     print(f"\n{pregunta["pregunta"]}")
    
#     if "opciones" in pregunta:
#         print("\nOpciones:")
#         for indice, opcion in enumerate(pregunta["opciones"], start=1):
#             print(f"{indice}. {opcion}")

#         while True:
#             rta = int(input("\nIngresa el numero de la opcion (0 para Salir): "))
#             if rta == 0:
#                 return 0
#             elif 1 <= rta <= len(pregunta["opciones"]):
#                 return pregunta["opciones"][rta - 1].capitalize()
#             else:
#                 print("Opcion no valida. Intenta de nuevo.")
#     else:
#         rta = input("Tu respuesta: ").capitalize()
#         return rta

# def jugarTrivia():
#     """
#     Función principal para jugar el juego de trivia.
#     """
#     print("========== Juego de Trivia ==========")
#     print("\nResponde correctamente a las preguntas para ganar puntos.")
#     print("Presiona 0 en cualquier momento para salir.\n")
    
#     puntaje = 0
#     totalPreguntas = len(preguntasTrivia)
    
#     random.shuffle(preguntasTrivia)
    
#     for indice, pregunta in enumerate(preguntasTrivia, start=1):
#         print(f"\nPregunta {indice} de {totalPreguntas}:")
        
#         rtaUsuario = mostrarPregunta(pregunta)
        
#         if rtaUsuario == "0":
#             print("\nHas decidido salir del juego. ¡Hasta luego!")
#             break
        
#         rtaCorrecta = pregunta["respuesta"].capitalize()
#         if rtaUsuario == rtaCorrecta:
#             print("¡Respuesta Correcta! +1 punto.")
#             puntaje += 1
#         else:
#             print(f"Respuesta Incorrecta. La respuesta correcta era: {rtaCorrecta}.")
    
#     print("\n====================")
#     print(f"Juego Terminado!")
#     print(f"Puntuación Final: {puntaje}/{totalPreguntas}")
#     print("====================")

# jugarTrivia()

