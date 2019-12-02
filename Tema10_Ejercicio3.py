import urllib.request

peticion = urllib.request.Request("http://www.google.com")
respuesta = urllib.request.urlopen(peticion)
pagina = respuesta.read()
file = open("C:/Users/rfernandezm/Desktop/fichero1.txt", "bw")
file.write(pagina)
file.close()

