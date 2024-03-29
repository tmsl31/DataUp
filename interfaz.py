#Interfaz del proyecto DataUp.

# Imports.
# Modulo de DataUp
from DataUp import *
# Tkinter.
from tkinter import *
# Grafico.
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

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
calificaciones = [0.,1.,2.];
fig_photo = 0;

#Definicion de funciones a utilizar en la interfaz.
def obtenerTiempo():
    #Funcion que obtenga el tiempo de grabacion.
        global tiempoGrab
        #Definicion de los metodos de la clase.
        tiempoGrab = int(tiempoIngresar.get())
        print(tiempoGrab)
        
def grabacion(tiempoGrab):
    #Funcion que realiza la grabacion.
    #Obtener el valor del tiempo de grabacion.
    #Llamar a visualizar
    global calificaciones
    try:
        caracteristicas2, calificaciones2 = procesarAudioTest(tiempoEspera = tiempoGrab)
        calificaciones = calificaciones2
        print(calificaciones)
    except:
        print('Error en la grabacion. Reintentar')
    print('Lista la conversion')
    return calificaciones
        

def matplotCanvas(caracteristicas,calificaciones):
    #Display del grafico en la interfaz.
    #Numero de caracteristicas
    AttNo = len(caracteristicas)
    #Creacion de la figura.
    f = Figure(figsize=(5,5),dpi = 100)
    ax = f.add_subplot(111, polar = True)
    #Definicion de los angulos.
    angles = [n / float(AttNo) * 2 * np.pi for n in range(AttNo)]
    angles += angles [:1]
    angles = np.array(angles)
    #
    calificaciones = np.append(calificaciones,calificaciones[:1])
    #Agregar los atributos al grafico.
    #Agregar valor al atributo.
    car = agregarValor(caracteristicas,calificaciones)
    #Angulos
    #plt.xticks(angles,car)  
    ax.set_thetagrids(angles * 180.0/np.pi, car)
    #
    ax.plot(angles,calificaciones,'o-')
    #Fill in the area plotted in the last line
    ax.fill(angles, calificaciones, 'teal', alpha=0.1)
    #Titulo.
    ax.set_title("Resultados encuesta")
    #Generar canvas
    canvas = FigureCanvasTkAgg(f,root)
    canvas.get_tk_widget().pack()

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
#Boton de display del grafico.
botonGrafico = Button(root, text = 'Mostrar Grafico', compound = LEFT, command =lambda: matplotCanvas(caracteristicas,calificaciones))
botonGrafico.place(x=160,y=200)

root.mainloop()