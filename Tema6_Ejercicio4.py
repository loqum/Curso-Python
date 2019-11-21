def imprimir(cadena, invertida = False, numero_veces = 1):
  mensaje = cadena[::-1] * numero_veces if invertida else cadena * numero_veces
  return mensaje

