import time
import os

def calcular_hora_cierre():
    hora = time.strftime("%H")
    minutos = time.strftime("%M")

    mensaje = "Es la hora de irse" if int(hora) >= 18 else f"Quedan {17- int(hora)} horas y {59- int(minutos)} minutos para irse a casa"

    return mensaje

print(calcular_hora_cierre())

"""def ping_to(url):
    print(os.system("ping " + url))


print(os.listdir())

ping_to("google.com")

print(os.urandom(5))
"""
