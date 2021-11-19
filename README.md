# blackjack

Mi direccion para acceder al repositorio es la siguiente: [GitHub](https://github.com/AnaLopezP/blackjack/edit/main/README.md)
https://github.com/AnaLopezP/blackjack/edit/main/README.md

En esta tarea hemos creado el juego BlackJack, en una partida del jugador frente a la máquina.
El diagrama de flujo que tenemos en nuestro codigo es el siguiente:

![diagrama de flujo Blackjack](Diagrama_de_flujo_Blackjack.JPG)

```
import random
baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#funcion para repartir cartas
def preparacion(baraja):
    primera_carta = random.choice(baraja)
    print(primera_carta)
    segunda_carta = random.choice(baraja)
    print(segunda_carta)
    puntuacion = primera_carta + segunda_carta
    
    return puntuacion

#funcion para que juegue el crupier
def crupier(baraja, puntuacion_crupier):
    while puntuacion_crupier < 17:
        nueva_carta_crupier = random.choice(baraja)
        puntuacion_crupier = puntuacion_crupier + nueva_carta_crupier
        print(puntuacion_crupier)
    print("El crupier se planta")

    return puntuacion_crupier

#funcion para que juegue el jugador
def player(baraja, puntuacion_jugador):
    print("¿Quieres una carta? ¿y o n?")
    respuesta = str(input())
    while respuesta == "y":
        nueva_carta_jugador = random.choice(baraja)
        print(nueva_carta_jugador)
        puntuacion_jugador = puntuacion_jugador + nueva_carta_jugador
        print("Tu nueva puntuacion es: " + str(puntuacion_jugador))
        print("¿Quieres otra carta? ¿y o n?")
        respuesta = str(input())
    print("El jugador se planta")
    return puntuacion_jugador

# cartas para eljugador
jugador = preparacion(baraja)
print("La puntuacion del jugador es: " + str(jugador))

#cartas para la banca
banca = preparacion(baraja)
print("La puntuacion del crupier es: " + str(banca))

#Turno de jugador
jugador = player(baraja, jugador)

#Turno de la banca
banca = crupier(baraja, banca)

#decision de quien gana
if banca > 21 and jugador > 21:
    print("Como nos hemos pasado, se queda en tablas.")
elif banca <= 21 and jugador <= 21:
    if banca > jugador:
        print("He ganado")
    elif banca == jugador:
        print("Hemos quedado empate")
    else:
        print("Me has superado. Has ganado, felicidades.")
else:
    if jugador > 21:
        print("Has perdido, te has pasado de 21 con: " + str(jugador))
    else:
        print("Te plantas con: " + str(jugador) + ". Has ganado")
    if banca > 21:
        print("He perdido, me he pasado de 21 con: " + str(banca))
    else:
        print("Me planto con: " + str(banca) + ". He ganado")
