from DataUp import *
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="DataUP")
        self.label.pack()

        self.rec_button = Button(master, text="Grabar", command=self.grabar)
        self.rec_button.pack()
    
        # Botón de parar
        self.stoprec_button = Button(master, text="Detener", command=self.detener)
        self.stoprec_button.pack()

        # Procesas
        self.proc_button = Button(master, text="Procesar", command=self.procesar)
        self.proc_button.pack()
        
    def grabar(self):
        print("Grabando...")
        obtenerGrafico(tiempoEspera = 30)
    def detener(self):
        print("Grabado")
        
    def procesar(self):
        print("Procesando...")
        
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()