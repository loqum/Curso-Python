from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.hello = Button(frame, text = "Hello", command = self.say_hello)
        self.hello.pack(side = LEFT)
        
    def say_hello(self):
        print("Hello everyone!")

root = Tk()
app = App(root)
root.mainloop()
