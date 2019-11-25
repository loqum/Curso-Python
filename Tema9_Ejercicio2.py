def tabla_numerada(final, inicio = 1, ancho_maximo = 3):
  for x in range(inicio, final + 1):
    resultado = ""
    i = 1
    while (i <= ancho_maximo):
      resultado += repr(x ** i).rjust(i * 2 * len(repr(final)))
      i += 1
    else:
      print(resultado)
