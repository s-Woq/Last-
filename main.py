import time
import random
#colors->

RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[39m'
GREEN = '\033[32m'

record = []
count = 0
round = 0
random = random.randint(2, 5)
z = 1

puntaje = 0
nombre = input("Cual es tu nombre? : ")
print(GREEN + "Bienvenido ", nombre,
      " Esta es una  trivia sobre Los pawer Rangers... ", RESET)
print("Pondremos a prueba tus conocimientos")
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Tienes", puntaje, "puntos")

trivia_start = True
attempts = 0
while trivia_start == True:
    attempts += 1
    puntaje = 0
    print("Numero de Intentos:", attempts, "!")
    input("Presiona enter para continuar")
    print(YELLOW + "Primera Pregunta : Quien es  el power ranger rojo?" +
          RESET)

    print(
        " a) Jason Lee \n b) Tobey Maguire \n c) Chris Rock \n d) Thomas the Train "
    )
    respuesta = input("Introduce tu respuesta aqui : ")
    while respuesta not in ("a", "b", "c", "d"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta = input("Tu respuesta Aqui:")
    if respuesta == "a":
        puntaje += 10

        print("...")
        print(GREEN + "Has obtenido ", puntaje, "puntos!" + RESET)
    else:
        puntaje -= 10
        print(RED + "Tu Puntaje es : ", puntaje, "puntos!" + RESET)

    record.append(puntaje)

    print(YELLOW +
          "Segunda pregunta : Desde cuando se emite los Power Rangers: " +
          RESET)

    print("  a) 2005 \n  b) 1993 \n  c) 2000 \n  d) 1892  ")
    respuesta2 = input("Introduce Tu respuesta Aqui: ")
    while respuesta2 not in ("a", "b", "c", "d"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta2 = input("Tu respuesta Aqui:")
    if respuesta2 == "b":
        puntaje += 15
        print("...")
        print(GREEN + "Has obtenido ", puntaje, "puntos!" + RESET)
    else:
        puntaje -= 10
        print("...")
        print(RED + "Tu Puntaje es : ", puntaje, "puntos!" + RESET)
    record.append(puntaje)

    print(YELLOW + "Tercera Pregunta: Donde se Grabo la serie?" + RESET)
    print(" a) Australia \n b) Irlanda \n c) EEUU \n d) Mexico ")
    respuesta3 = input("Tu respuesta aqui : ")
    while respuesta3 not in ("a", "b", "c", "d", "x"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta3 = input("Tu respuesta Aqui:")

    if respuesta3 == "c":
        puntaje += 20
        print("...")
        print(GREEN + "Has obtenido ", puntaje, "puntos!" + RESET)
    elif respuesta3 == "x":
        puntaje += 30
        print("Felicidades Descubriste una respuesta secreta ... ")

    else:
        puntaje -= 10
        print("...")
        print(RED + "Tu Puntaje es : ", puntaje, "puntos!" + RESET)
    record.append(puntaje)

    randomp = input(
        YELLOW +
        'Quieres Incrementar tu puntaje? Ingresa "si" si deseas intentarlo :' +
        RESET)
    if randomp == "si":
        puntaje = puntaje * random
        print("Felicidades tu nuevo puntaje es ... : ", puntaje)

    for i in record:

        count += 1
        print("Estos son los puntajes obtenidos durante el juego -> ", count,
              " :", i)

    try_again = input(
        'Quieres repetir la trivia? Ingresa "si" para continuar o cualquier otra tecla para finalizar ... '
    ).lower()

    if try_again == "si":
        count = 0
        round += 1
        z += 1

    if try_again != "si":
        print("Espero te haya gustado la trivia ", nombre, " , Hasta Pronto!")
        trivia_start = False
