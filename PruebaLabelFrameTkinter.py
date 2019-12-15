from tkinter import *

class App:
    def __init__(self, master):
        labelFrame = LabelFrame(master, height = 100, width = 100, text="Prueba LabelFrame")
        labelFrame.pack()
        self.hello = Button(labelFrame, text = "Hello", command = self.say_hello)
        self.hello.pack(side = LEFT)
        label_hello = Label(text = self.say_hello)
        label_hello.pack()

    def say_hello(self):
        return "Holi"

root = Tk()
app = App(root)
root.mainloop()
