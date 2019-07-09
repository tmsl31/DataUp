#Dataup Final.

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

#Funciones globales.
def crearMatriz(caract):
    n = len(caract)
    Mat = np.zeros((1, n))
    return Mat

def almacenar(vec, Mat): 
    Mat = np.vstack((Mat,vec))
    return Mat

def generarCSV(M,directorio):
	B = pd.DataFrame(M)
	B.to_csv(directorio,header=None,sep=';')

#Variables globales.
#Valor del tiempo de grabacion (default =30)
tiempoGrab = 30;
#Caracteristicas.
caracteristicas = ['dulce','amargo','burbuja'];
#Calificaciones.
calificaciones = [0.,1.,2.];
#
fig_photo = 0;
#Crear la matriz.
matrizDatos = crearMatriz(caracteristicas)
#directorio PC.
directorio = "C:/Users/tlara/OneDrive/Documentos/GitHub/DataUp/DataUpDB.csv"

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
    global calificaciones, matrizDatos
    try:
    	#Procesar audio.
        caracteristicas2, calificaciones = procesarAudioTest(tiempoEspera = tiempoGrab)
        #Agregar datos a la matriz.
        matrizDatos = almacenar(calificaciones,matrizDatos);
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
#Nombre de dataup.
NombreApp = Label(root, text="Data Up", font=('Helvetica', 18, "bold"))
NombreApp.pack(side = TOP, )
#Etiqueta de ingreso de datos.
etiquetaIngreso = Label(root, text='Tiempo de grabación')
etiquetaIngreso.pack(side = TOP)
#Ventana de ingreso de texto
tiempoIngresar = Entry()
tiempoIngresar.pack(side = TOP)
#Boton de set tiempo.
botonSet = Button(root, text='Set', command =lambda: obtenerTiempo())
botonSet.pack(side = TOP)
#Boton de grabar.
fotoMic= PhotoImage(file=r"C:/Users/tlara/OneDrive/Documentos/GitHub/DataUp/microphone.png")
fotoMic2 = fotoMic.subsample(5,5)
botonGrabar = Button(root, text = 'Grabar!', image = fotoMic2, compound = LEFT, command =lambda: grabacion(tiempoGrab))
botonGrabar.pack(side = TOP)
#Boton de display del grafico.
botonGrafico = Button(root, text = 'Mostrar Grafico', compound = LEFT, command =lambda: matplotCanvas(caracteristicas,calificaciones))
botonGrafico.pack(side = TOP)
#Boton de almacenamiento de datos.
botonCSV = Button(root, text = 'GeneraCSV', compound = LEFT, command =lambda: generarCSV(matrizDatos,directorio))
botonCSV.pack(side = TOP)


root.mainloop()