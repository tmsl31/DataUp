#nterfaz del proyecto DataUp.

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

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
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
        try:
            caracteristicas, calificaciones = procesarAudio(tiempoEspera = tiempoGrab)
        except:
            print('Error en la grabacion. Reintentar')
        #Cambiar a la pagina del grafico.
        master.switch_frame(PlotPage)
            
    def matplotCanvas(caracteristicas,calificaciones):
        #Display del grafico en la interfaz.
        #Transicion a la pagina del grafico.
        
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

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Data Up", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Realizar una Grabación",command=lambda: master.switch_frame(RecordPage)).pack()
        Button(self, text="Ver Datos registrados",command=lambda: master.switch_frame(DataPage)).pack()
        
class RecordPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='lightblue')
        Label(self, text="Data Up", font=('Helvetica', 18, "bold")).pack(side=TOP, expand = True, fill=X)
        Button(self, text="Volver principal", command=lambda: master.switch_frame(StartPage)).pack(side="top", fill="x", pady=5)
        #Etiqueta de ingreso de datos.
        self.etiquetaIngreso = Label(self, text='Tiempo de grabación').pack(side=TOP)
        #Ventana de ingreso de texto
        self.tiempoIngresar = Entry(self).pack(side=TOP)
        #Boton de set tiempo.
        self.botonSet = Button(self, text='Set', command =lambda: master.obtenerTiempo(tiempoGrab)).pack(side=TOP)
        #Boton de grabar.
        self.fotoMic= PhotoImage(file=r"C:\Users\tlara\OneDrive\Documentos\GitHub\DataUp\microphone.png")
        self.fotoMic2 = self.fotoMic.subsample(5,5)
        self.botonGrabar = Button(self, text = 'Grabar!', image = self.fotoMic2, compound = LEFT, command =lambda: master.grabacion(tiempoGrab)).pack(side=BOTTOM, fill="x", pady=5)


class PlotPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='red')
        Label(self, text="Resultado encuesta", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Volver principal",command=lambda: master.switch_frame(StartPage)).pack(side=TOP)
                #Boton de display del grafico.
        self.botonGrafico = Button(self, text = 'Mostrar Grafico', compound = LEFT, command =lambda: master.matplotCanvas(caracteristicas,calificaciones)).pack(side=TOP)
        
class DataPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='red')
        Label(self, text="Datos recopilados", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Volver principal",command=lambda: master.switch_frame(StartPage)).pack()            
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()   