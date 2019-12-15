from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.height = 10
        frame.width = 10
        frame.pack()
        self.hello = Button(frame, text = "Hello", command = self.say_hello)
        self.hello.pack(side = LEFT)
        self.label_hello = Label(frame, text = self.say_hello)
        self.label_hello.pack(side = LEFT)

    def say_hello(self):
        return "Hello everyone!"

root = Tk()
app = App(root)
root.mainloop()
