#Modulo de visualizacion.
#Imports.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib as mpl

#Funcion para agregar el valor de la calificacion al tipo de calificacion
#(solo para visualizarlo mas facilmente)
def agregarValor(caracteristicas,calificaciones):
    #Funcion que genere una lista de strings con caracteristica y calificacion para la visualizacion de la informacion.
    
    #Vector vacio.
    vecGraph = np.array([]);
    #Ir concatenando.
    count = 0
    for caracteristica in caracteristicas:
        agregar = caracteristica + '(' + str(calificaciones[count]) +')'
        vecGraph = np.append(vecGraph,agregar)
        count += 1;
    return vecGraph

#Funcion que muestre el grafico de radar.
def visualizacion(caracteristicas, calificaciones):
    #Visualizacion rapida de caracteristicas
    
    #Numero de calificaciones.
    AttNo = len(caracteristicas)
    #Generacion del grafico.
    ax = plt.subplot(111, polar = True)
    #Definicion de los angulos.
    angles = [n / float(AttNo) * 2 * np.pi for n in range(AttNo)]
    angles += angles [:1]
    #
    calificaciones = np.append(calificaciones,calificaciones[:1])
    #Agregar los atributos al grafico.
    #Agregar valor al atributo.
    car = agregarValor(caracteristicas,calificaciones)
    plt.xticks(angles,car)
    #
    ax.plot(angles,calificaciones)
    #
    #Fill in the area plotted in the last line
    ax.fill(angles, calificaciones, 'teal', alpha=0.1)
    #Titulo.
    ax.set_title("Resultados encuesta")
    plt.show()

def visualizacion2(caracteristicas,calificaciones):
    #Visualizacion del grafico de radar.
    AttNo = len(caracteristicas)
    #Creacion del grafico.
    ax = plt.subplot(111, polar = True)
    #Definicion de los angulos.
    angles = [n / float(AttNo) * 2 * np.pi for n in range(AttNo)]
    angles += angles [:1]
    #
    calificaciones = np.append(calificaciones,calificaciones[:1])
    #Agregar los atributos al grafico.
    #Agregar valor al atributo.
    car = agregarValor(caracteristicas,calificaciones)
    plt.xticks(angles,car)
    #
    ax.plot(angles,calificaciones,'o-')
    #Fill in the area plotted in the last line
    ax.fill(angles, calificaciones, 'teal', alpha=0.1)
    #Titulo.
    ax.set_title("Resultados encuesta")
    #Guardar figura.
    plt.savefig('grafico.png')
