def recursiva(numero):
    if (numero != 0 and numero != 1):
        numero = recursiva(numero - 1) + recursiva(numero - 2)
    return numero

print(recursiva(6))
