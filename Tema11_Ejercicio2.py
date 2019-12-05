lista1 = list(range(10))
lista2 = list(range(-5, 5))

lista_restada = list(map(lambda x: x - 5, lista1))
lista_elevada = list(map(lambda x: x ** 3, lista2))

print(dict(zip(lista_restada, lista_elevada)))
