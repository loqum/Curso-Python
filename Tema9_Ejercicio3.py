NAME_FILE = "create_write.txt"

def crear_escribir(name_file):
  file = open(name_file, "w")
  file.write("sample sample sample\n")
  file.close()

def seguir_escribiendo(name_file):
  i = 1
  file = open(name_file, "r+")
  file.readline()
  while (i <= 10):
    file.write("Ya he escrito " + str(i) + " veces")
  file.seek(0)
  print(file.read())
  file.close()

#crear_escribir(NAME_FILE)
seguir_escribiendo(NAME_FILE)

