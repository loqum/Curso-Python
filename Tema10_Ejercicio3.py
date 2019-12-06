import urllib.request

PATH_DESKTOP = "C:/Users/ruben/Desktop/"

peticion = urllib.request.Request("http://www.google.com")
respuesta = urllib.request.urlopen(peticion)
pagina = respuesta.read()
file = open(PATH_DESKTOP + "fichero1.txt", "bw")
file.write(pagina)
file.close()
