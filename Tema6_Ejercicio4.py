def imprimir(cadena, invertida = False, numero_veces = 1):
  mensaje = cadena[::-1] * numero_veces if invertida else cadena * numero_veces
  return mensaje

print(imprimir("Curso Python", True, 5))
print(imprimir("Curso Python", False, 2))
print(imprimir("Curso Python", True))
print(imprimir("Curso Python", False))
print(imprimir("Curso Python"))
