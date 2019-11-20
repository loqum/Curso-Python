fin = 1
def funcion1():
    global fin
    if fin <= 10:
        fin = fin + 1
        funcion2()
    print("Estoy en la funcion1")

def funcion2():
    global fin
    if fin <= 10:
        fin = fin + 1
        funcion1()
    print("Estoy en la funcion2")

funcion1()
