import random

def adivina_numero():
    numero_a_adivinar = random.randint(1, 100)
    max_intentos = 10
    intentos = 0

    while intentos < max_intentos:
        intentos += 1
        numero_ingresado = int(input("Intento {0}: Ingresa un número entre 1 y 100: ".format(intentos)))

        if numero_ingresado < numero_a_adivinar:
            print("El número ingresado es menor que el número a adivinar.")
        elif numero_ingresado > numero_a_adivinar:
            print("El número ingresado es mayor que el número a adivinar.")
        else:
            print("¡Felicidades! Adivinaste el número en {0} intentos.".format(intentos))
            break


    if intentos == max_intentos:
        print("Lo siento, has superado el límite de intentos. El número a adivinar era {0}.".format(numero_a_adivinar))

adivina_numero()
