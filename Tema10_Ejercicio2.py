import math
from decimal import Decimal

def calcular_angulos(cateto1, cateto2, cateto3):
  dos = Decimal('2')
  return math.degrees(math.acos((cateto3**dos + cateto2**dos - cateto1**dos) / (dos * cateto2 * cateto3)))

def triangulo(cateto1, cateto2, cateto3):
  cateto1 = Decimal(f'{cateto1}')
  cateto2 = Decimal(f'{cateto2}')
  cateto3 = Decimal(f'{cateto3}')

  angulo_A = calcular_angulos(cateto1, cateto2, cateto3)
  angulo_B = calcular_angulos(cateto2, cateto3, cateto1)
  angulo_C = calcular_angulos(cateto3, cateto1, cateto2)
  return [angulo_A, angulo_B, angulo_C]


print(triangulo(5, 3, 4))