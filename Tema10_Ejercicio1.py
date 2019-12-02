import shutil

def escribir_leer_archivo:
  file = open("C:/Users/rfernandezm/Desktop/fichero1.txt", "w")
  file.write("Hola mundo")
  print(file.read())
  file.close()

def sobreescribir_archivo:
  file = open("C:/Users/rfernandezm/Desktop/fichero1.txt", "a")
  file.write("Hola mundo.\n")
  file.close()

def mover_archivo(url_file_original, url_file_destiny):
  shutil.move("C:/Users/rfernandezm/Desktop/fichero1.txt", "C:/Users/rfernandezm/Documents/fichero1.txt")