from tkinter import *
class App:
    def __init__(self, master):
        frame = Frame(master)
        label = Label(text = 'Animales')
        listbox = Listbox()
        listbox.insert(0, ('Perro'))
        listbox.insert(1, ('Gato'))
        listbox.insert(2, ('Orangutan'))
        listbox.insert(3, ('Paloma'))
        listbox.insert(4, ('Vaca'))
        listbox.insert(5, ('Cerdo'))
        listbox.insert(6, ('Canguro'))
        label.pack()
        listbox.pack()
        frame.pack()

root = Tk()
app = App(root)
root.mainloop()
