#nterfaz del proyecto DataUp.

# Imports.
# Modulo de DataUp
from DataUp import *
# Tkinter.
from tkinter import *
# Grafico.
import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

#Define la interfaz como una clase.
class ventanaDataUp:
    def __init__(self, win):
        #Etiqueta de ingreso de datos.
        self.etiquetaIngreso = Label(win, text='Tiempo de grabación')
        self.etiquetaIngreso.place(x=50, y=50)
        #Ventana de ingreso de texto
        self.tiempoIngresar = Entry()
        self.tiempoIngresar.place(x=170, y=50)
        #Boton de set tiempo.
        self.botonSet = Button(win, text='Set')
        self.botonSet.place(x = 300, y = 48)
        #Boton de grabar.
        self.fotoMic= PhotoImage(file=r"C:\Users\tlara\OneDrive\Documentos\GitHub\DataUp\microphone.png")
        self.fotoMic2 = self.fotoMic.subsample(5,5)
        self.botonGrabar = Button(win, text = 'Grabar!', image = self.fotoMic2, compound = LEFT, command = self.grabacion)
        self.botonGrabar.place(x=160,y=100)
        win.config(bg="gray") #Cambiar color de fondo
        
    #Definicion de los metodos de la clase.
    def grabacion(self):
        #Obtener el valor del tiempo de grabacion.
        tiempoGrabacion = int(self.tiempoIngresar.get())
        #Llamar a visualizar
        obtenerGrafico(tiempoEspera = tiempoGrabacion)
        
    def displayResultados(self):
        print('Obteniendo grafico')
        
    def draw_figure(canvas, figure, loc=(50, 300)):
        figure_canvas_agg = FigureCanvasAgg(figure)
        figure_canvas_agg.draw()
        figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

        # Position: convert from top-left anchor to center anchor
        canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

        # Unfortunately, there's no accessor for the pointer to the native renderer
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

        # Return a handle which contains a reference to the photo object
        # which must be kept live or else the picture disappears
        return photo
    

        
window=Tk()
mywin=ventanaDataUp(window)
window.title('DataUp')
window.geometry("400x300+10+10")
window.mainloop()