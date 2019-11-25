from pickle import * 

class Persona:

  def __init__(self, nombre, apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
  
  def __str__(self):
    return self.nombre + " " + self.apellidos

ruben = Persona("Ruben", "Fernandez Moreno")
print(ruben)

file = open("ruben_objeto", "w+b")

dump(ruben, file)

file.seek(0)

nuevo_ruben = load(file)
print(nuevo_ruben)
file.close()
