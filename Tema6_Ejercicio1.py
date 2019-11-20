def concatena_palabras_ordenadas(palabra1, palabra2):
    return palabra1 + palabra2 if (len(palabra1) >= len(palabra2)) else palabra2 + palabra1

print(concatena_palabras_ordenadas("Pamplona ", "Vitoria "))
