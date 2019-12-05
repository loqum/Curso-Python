from functools import reduce

def get_numeros_impares(lista):
  lista_numeros_impares = list(filter((lambda x: x%2), lista))
  lista_numeros_total = reduce((lambda x, y: x + y), lista_numeros_impares)
  return lista_numeros_total

numeros = list(range(100))

print(get_numeros_impares(numeros))