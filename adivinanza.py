#Importamos random para que nos genere numero aleatorio
import random
#definimos la variable adivinanza, para asignarle los valores que se mostraran
def adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
#la condicion while se hara bucle hasta que se cumpla una condicion
    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1
#aca mencionamos que el intento se aumentara ademas no concuerda con el numero secreto
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
#igual el intento es demasiado alto, y ademas se suma porque se hace bucle
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
#si lo logramos, se manda a imprimir felicidades
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
#Para que se verifique que no es modulo, best practices
if __name__ == "__main__":
    adivinanza()
