class Persona:
  def __init__(self, nombre, primer_apellido, segundo_apellido):
    self.nombre = nombre
    self.primer_apellido = primer_apellido
    self.segundo_apellido = segundo_apellido

  def mostrar_nombre(self):
    print(self.nombre)
  
  def mostrar_apellidos(self):
    print(self.primer_apellido)
    print(self.segundo_apellido)
  
  def __str__(self):
    return "Nombre: " + self.nombre + ", \nApellidos: " + self.primer_apellido + " " + self.segundo_apellido

class Empleado(Persona):
  numero_empleados = 0

  def __init__(self, nombre, primer_apellido, segundo_apellido, **clientes):
    super().__init__(nombre, primer_apellido, segundo_apellido)
    self.clientes = clientes
    Empleado.numero_empleados += 1
    self.numero_empleado = Empleado.numero_empleados
  
  def mostrar_clientes(self):
    for num, cliente in self.clientes.items():
      print("Cliente ", num, ", ", cliente)
  
  def mostrar_numero_empleado(self):
    print(self.numero_empleado)

class Cliente(Persona):
  numero_clientes = 0
  def __init__(self, nombre, primer_apellido, segundo_apellido, direccion):
    super().__init__(nombre, primer_apellido, segundo_apellido)
    self.direccion = direccion
    Cliente.numero_clientes += 1
    self.numero_cliente = Cliente.numero_clientes
  
  def print_direccion(self):
    print(self.direccion)

  def print_numero_cliente(self):
    print(self.numero_cliente)
    
  def __str__(self):
    return super().__str__() + ", \nDireccion: " + self.direccion
  
empleados = {}
clientes = {}

def crearEmpleados():
  global empleados
  nombre = input("Introduce el nombre: ")
  primer_apellido = input("Introduce el primer apellido: ")
  segundo_apellido = input("Introduce el segundo apellido: ")
  empleado = Empleado(nombre, primer_apellido, segundo_apellido)
  empleados[empleado.numero_empleado] = empleado

def crearClientes():
  global clientes
  nombre = input("Introduce el nombre: ")
  primer_apellido = input("Introduce el primer apellido: ")
  segundo_apellido = input("Introduce el segundo apellido: ")
  direccion = input("Introduce la direccion: ")
  cliente = Cliente(nombre, primer_apellido, segundo_apellido, direccion)
  clientes[cliente.numero_cliente] = cliente

def print_clientes():
  global clientes
  for numero, cliente in clientes.items():
    print("Cliente: ", numero, ", ", cliente)

def print_empleados():
  global empleados
  for numero, empleado in empleados.items():
    print("Empleado: ", numero, ", ", empleado)

def clientesEmpleados():
  global empleados
  try:
    numero_empleado = int(input("Introduce el número de empleado: "))
    empleados[numero_empleado].mostrar_clientes()
  except TypeError:
    print("El numero de empleado no existe")

def add_cliente():
  global clientes, empleados
  try:
    numero_empleado = int(input("Introduce el numero de empleado: "))
    numero_cliente = int(input("Introduce el numero de cliente: "))
    empleado = empleados[numero_empleado]
    cliente = clientes[numero_cliente]
    empleado.clientes[numero_cliente] = cliente
  except TypeError:
    print("Numero incorrecto")

def mensaje_finalizar():
  print("Finalizando...")

def switch(opcion):
  switcher = {
    1 : crearEmpleados,
    2 : crearClientes,
    3 : print_empleados,
    4 : print_clientes,
    5 : clientesEmpleados,
    6 : add_cliente,
    0 : mensaje_finalizar,
  }

  func = switcher.get(opcion, "Opcion no valida")
  func()

opciones = """ 
    Opción 1 : Crear Empleado
    Opción 2 : Crear Cliente
    Opción 3 : Ver Lista Empleados
    Opción 4 : Ver Lista Clientes
    Opción 5 : Ver Clientes de Empleado
    Opción 6 : Asignar Clientes a Empleado
 
    Opción 0 : Salir"""

opcion = ""

while (opcion != 0):
  print(opciones)
  try:
    opcion = int(input("Introduce una opcion: "))
    switch(opcion)
  except:
    print("Opcion no valida")
