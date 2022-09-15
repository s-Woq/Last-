import time
from random import randint
from datetime import datetime
import pytz
import os


def clear():
  os.system('clear')

RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[39m'
GREEN = '\033[32m'
def countries_random():
  random_country=randint(0,9)
  countries=['Asia/Seoul','America/New_York','US/Central', 'Europe/Athens','America/Lima','America/Vancouver','Europe/Vienna','US/Arizona','America/Argentina/Buenos_Aires', 'America/Santiago']
  
  distance = ['16.296 km','5871 km', "who knows :)", '11.758 km', '0km', '8165 km', '11.247 km','5789 km','3,937.1 km', '3,287.0 km']
  
  
  #UTC = pytz.utc
  requested_location = pytz.timezone(countries[random_country])
  name_of_country = countries[random_country] 
  print(YELLOW +name_of_country + RESET, "is" , distance[random_country],"away!")
  date_time_utc=datetime.now(requested_location)
  
  print("  Current time somewhere else in the planet:", "(",countries[random_country],')'+"\n",GREEN,date_time_utc.strftime( "Time -> H: %H : M: %M : S: %S"),RESET)
  


#colors->



  


countries_random()

record = []
count = 0
round = 1
random = randint(2, 5)
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
    print(GREEN + "ROUND" , round)
    countries_random()
    attempts += 1
    puntaje = 0
    print("Numero de Intentos:", attempts, "!")
    input("Presiona enter para continuar")
    print(YELLOW + "Primera Pregunta : Quien es  el power ranger rojo?" +
          RESET)

    print(
        " a) Jason Lee \n b) Tobey Maguire \n c) Chris Rock \n d) Thomas the Train "
    )
    respuesta = input("Introduce tu respuesta aqui : ").lower()
    while respuesta not in ("a", "b", "c", "d"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta = input("Tu respuesta Aqui:").lower()
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
    respuesta2 = input("Introduce Tu respuesta Aqui: ").lower()
    while respuesta2 not in ("a", "b", "c", "d"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta2 = input("Tu respuesta Aqui:").lower()
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
    respuesta3 = input("Tu respuesta aqui : ").lower()
    while respuesta3 not in ("a", "b", "c", "d", "x"):
        print("Elige entre una opcion valida  a , b , c , d ")
        respuesta3 = input("Tu respuesta Aqui:").lower()

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
        RESET).lower()
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
        clear()
    

    if try_again != "si":     
      print("Espero te haya gustado la trivia ", nombre, " , Hasta Pronto!")
      trivia_start = False
