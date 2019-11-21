def concatVar(*cadenas):
  cadena = ""

  for i in cadenas:
    cadena += i
  
  return(cadena)

print(concatVar("Ruben", " Fernandez"))
print(concatVar("Ruben", " Fernandez", " Moreno"))