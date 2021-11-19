
import random
baraja = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def preparacion(baraja):
    primera_carta = random.choice(baraja)
    print(primera_carta)
    segunda_carta = random.choice(baraja)
    print(segunda_carta)
    puntuacion = primera_carta + segunda_carta
    
    return puntuacion

def crupier(baraja, puntuacion_crupier):
    while puntuacion_crupier < 17:
        nueva_carta_crupier = random.choice(baraja)
        puntuacion_crupier = puntuacion_crupier + nueva_carta_crupier
        print(puntuacion_crupier)
    print("El crupier se planta")

    return puntuacion_crupier

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


jugador = preparacion(baraja)
print("Esta es tu puntuación jugador : " + str(jugador))
banca = preparacion(baraja)
print("Esta es tu puntuación banca: " + str(banca))

jugador = player(baraja, jugador)
banca = crupier(baraja, banca)
