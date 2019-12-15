from tkinter import *
ventana=Tk()
ventana.title("Ejemplo eventos")
def mostrarDatos():
    texto1 = Label(ventana, text='Bienvenido!!! ').place(width=300,x=0,y=20)
    texto2 = Label(ventana, text='Al curso de Python').place(width=300,x=0,y=50)
ventana = Frame(height=250,width=300)
ventana.pack(padx=10,pady=10)
boton = Button(text="Mostrar Información",command=mostrarDatos).place(width=150, x=75,y=100)
ventana.mainloop()
