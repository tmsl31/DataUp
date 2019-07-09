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

#Definion de la interfaz.
root = Tk()
#Cambiar color de fondo
root.config(bg="lightblue") 
root.wm_title("DataUp")

#Valor del tiempo de grabacion (default =30)
tiempoGrab = 30;
#Caracteristicas.
caracteristicas = ['dulce','amargo','burbuja'];
#Calificaciones.
calificaciones = [0,1,2];
fig_photo = 0;

#Definicion de funciones a utilizar en la interfaz.
def obtenerTiempo(tiempoGrab):
    #Funcion que obtenga el tiempo de grabacion.
        #Definicion de los metodos de la clase.
        tiempoGrab = int(tiempoIngresar.get())
        print(tiempoGrab)
        
def grabacion(tiempoGrab):
    #Funcion que realiza la grabacion.
    #Obtener el valor del tiempo de grabacion.
    #Llamar a visualizar
    caracteristicas, calificaciones = procesarAudio(tiempoEspera = tiempoGrab)
    

def displayGrafico(caracteristicas,calificaciones):
    #Display del grafico en la interfaz.
    # Generar la figura.
    figura = visualizacion2(caracteristicas,calificaciones)
    #
    # Keep this handle alive, or else figure will disappear
    fig_x, fig_y = 100, 100
    fig_photo = draw_figure(canvas, figura, loc=(fig_x, fig_y))
    fig_w, fig_h = fig_photo.width(), fig_photo.height()


#Interfaz.
#Etiqueta de ingreso de datos.
etiquetaIngreso = Label(root, text='Tiempo de grabación')
etiquetaIngreso.place(x=50, y=50)
#Ventana de ingreso de texto
tiempoIngresar = Entry()
tiempoIngresar.place(x=170, y=50)
#Boton de set tiempo.
botonSet = Button(root, text='Set', command =lambda: obtenerTiempo(tiempoGrab))
botonSet.place(x = 300, y = 48)
#Boton de grabar.
fotoMic= PhotoImage(file=r"C:\Users\tlara\OneDrive\Documentos\GitHub\DataUp\microphone.png")
fotoMic2 = fotoMic.subsample(5,5)
botonGrabar = Button(root, text = 'Grabar!', image = fotoMic2, compound = LEFT, command =lambda: grabacion(tiempoGrab))
botonGrabar.place(x=160,y=100)
#Creacion del canvas.
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
#Boton de display del grafico.
botonGrafico = Button(root, text = 'Mostrar Grafico', compound = LEFT, command =lambda: displayGrafico(caracteristicas,calificaciones))
botonGrafico.place(x=160,y=200)


#Correr la interfaz
root.mainloop()