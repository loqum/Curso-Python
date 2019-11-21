class Persona:
  nombre = ""
  primer_apellido = ""
  segundo_apellido = ""

  def print_persona(self, nombre, primer_apellido, segundo_apellido):
    print(self.nombre)
    print(self.primer_apellido)
    print(self.segundo_apellido)
  
  def __init__(self, nombre = "", primer_apellido = "", segundo_apellido = ""):
    self.nombre = nombre
    self.primer_apellido = primer_apellido
    self.segundo_apellido = segundo_apellido
  
  def __str__(self):
    return self.nombre

ruben = Persona()
ruben.nombre = "Ruben"
ruben.primer_apellido = "Fernandez"
ruben.segundo_apellido = "Moreno" 
ruben.print_persona(ruben.nombre, ruben.primer_apellido, ruben.segundo_apellido)
jaime = Persona("Jaime", "Gutierrez", "Lozano")
