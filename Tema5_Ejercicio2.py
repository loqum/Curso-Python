x = 1
numeros_pares = []
numeros_impares = []

while (x <= 100):
    if (x%2 == 0):
        numeros_pares.append(x)
    else:
        numeros_impares.append(x)
    x+=1

for i in numeros_pares:
    print("Pares: ", i)

for i in numeros_impares:
    print("Impares: ", i)
