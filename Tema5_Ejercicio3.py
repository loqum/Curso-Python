from random import *

def genera_numero_aleatorio(minimo, maximo):

  try:
    if (minimo > maximo):
      aux = minimo
      minimo = maximo
      maximo = aux

    return randint(minimo, maximo)
  except TypeError:
    print("Debes escribir numeros")
    return -1

def encuentra_numero_aleatorio(numero_generado):
  encontrado = False
  intentos = 0

  while (not encontrado):
    numero_usuario = int(input("Introduce un numero: "))

    if (numero_usuario > numero_generado):
      print("El numero que has introducido es mayor que el numero generado. Sigue intentandolo.")
      intentos+=1
    elif (numero_usuario < numero_generado):
      print("El numero que has introducido es menor que el numero generado. Sigue intentandolo.")
      intentos+=1
    else:
      print("NUMERO CORRECTO!")
      print("\nLo has conseguido en: ", intentos, " intentos.")
      encontrado = True

encuentra_numero_aleatorio(genera_numero_aleatorio(1, 100))
