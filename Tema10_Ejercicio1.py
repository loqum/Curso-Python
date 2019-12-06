import shutil

PATH_DESKTOP = "C:/Users/ruben/Desktop/"
PATH_DOCUMENTS = "C:/Users/ruben/Documents/"

def escribir_leer_archivo(file_name, text):
  file = open(PATH_DESKTOP + file_name, "w")
  file.write(text)
  file.close()

def leer_archivo(file_name):
    file = open(PATH_DESKTOP + file_name, "r")
    print(file.read())

def sobreescribir_archivo(file_name, text):
  file = open(PATH_DESKTOP + file_name, "a")
  file.write(text + "\n")
  file.close()

def mover_archivo(file_name, url_file_original, url_file_destiny):
  shutil.move(url_file_original + file_name, url_file_destiny + file_name)

escribir_leer_archivo("archivo.txt", "Hola mundo!")
leer_archivo("archivo.txt")
sobreescribir_archivo("archivo.txt", "Hola, vecino")
