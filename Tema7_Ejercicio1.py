class Cliente:
    nombre = ""
    primer_apellido = ""
    segundo_apellido = ""

    def __init__(self, nombre = "", primer_apellido = "", segundo_apellido = ""):
        self.nombre = nombre;
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido

    def __str__(self):
        return self.nombre

    def print_cliente(self, nombre, primer_apellido, segundo_apellido):
        print(self.nombre, self.primer_apellido, self.segundo_apellido)

x = Cliente("Claudia", "García", "Pollastre")

x.print_cliente(x.nombre, x.primer_apellido, x.segundo_apellido)
