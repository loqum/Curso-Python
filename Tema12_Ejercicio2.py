from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    monitor.config(text = "")

root = Tk()
opcion = StringVar()
opcion.set(None)

LISTA_DNI = ['78038744C', '98916687N', '36627146Z', '05762484H', '01257847T', '87565847V',
             '15956061H', '10423402D', '90194506Y', '95496536F', '99181971Z', '54361447G']

for item in sorted(LISTA_DNI):
    Radiobutton(root, text=item, variable=opcion, value=item,
                command=seleccionar).pack(anchor=W)

Button(root, text = "Reset", command = reset).pack()

monitor = Label(root)
monitor.pack()
root.mainloop()
