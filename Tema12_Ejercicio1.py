from tkinter import *

class App:
    def __init__(self, master):
        LISTA_POLIGONOS = ["Cuadrado", "Triangulo", "Pentagono", "Heptagono", "Octagono", "Circulo"]
        frame = Frame(master)
        label = Label(text = "Poligonos")
        listbox = Listbox()
        for item in sorted(LISTA_POLIGONOS):
            listbox.insert(END, item)
        frame.pack()
        label.pack()
        listbox.pack()

root = Tk()
app = App(root)
root.mainloop()
