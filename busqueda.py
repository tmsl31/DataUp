#MODULO DE BUSQUEDA.

#Imports.
import numpy as np
import pandas as pd

def stringNumerico (word):
    #Funcion que verifica si un string es numerico
    try:
        val = int(word)
        output = True
    except ValueError:
        output = False
    return output

#Funcion que realiza la busqueda de la calificacion.
def buscarValorAsociado(caracteristica, vectorTexto):
    indiceCaracteristica = np.where(vectorTexto == caracteristica)
    calificacion = int(vectorTexto[indiceCaracteristica[0]+1])
    return calificacion

def buscarDespues(indiceCar,vecCaracteristicas,text,maxVentana):
    #Funcion que realiza busqueda hacia adelante.
    
    #Entregables.
    cond = False;
    calificacion = 'NS/NR'
    #Valores de indice.
    valoresIndice = np.arange(indiceCar+1,indiceCar+maxVentana)
    #Largo del texto.
    largoTexto = text.shape[0]
    #Ciclo de busqueda
    for indice in valoresIndice:
        if (indice >= largoTexto):
            #Caso en que el indice supere el largo del texto.
            break
        elif (text[indice] in vecCaracteristicas):
            #Caso en que se encuentre con otra caracteristica.
            break
        else:
            #Caso en que la palabra no es una caracteristica.
            if (stringNumerico(text[indice])):
                #Caso en que el string es un string numerico.
                cond = True
                calificacion = int(text[indice])
                break
                
    return cond,calificacion

def buscarAntes(indiceCar,vecCaracteristicas,text,maxVentana):
    #Funcion que realiza busqueda hacia adelante.
    
    #Entregables.
    cond = False;
    calificacion = 'NS/NR'
    #Valores de indice.
    indiceFinal = indiceCar-maxVentana
    valoresIndice = np.arange(indiceCar-1,indiceFinal, -1)
    #Ciclo de busqueda
    for indice in valoresIndice:
        if (indice < 0):
            #Caso en que el indice llegue a valores negativos.
            break
        elif (text[indice] in vecCaracteristicas):
            #Caso en que se encuentre con otra caracteristica.
            break
        else:
            #Caso en que la palabra no es una caracteristica.
            if (stringNumerico(text[indice])):
                #Caso en que el string es un string numerico.
                cond = True
                calificacion = int(text[indice])
                break
                
    return cond,calificacion
    
def buscarCalificacion(caracteristica,vecCaracteristicas,texto,maxVentana = 3):
    #Funcion que busque la calificacion asociada a una caracteristica.
    
    #Pasar a arreglo de numpy.
    text = np.array(texto)
    #Buscar la/las posicion/posiciones de la característica.
    indices = np.where(text==caracteristica);
    for indiceCar in indices:
        cond,calificacion = buscarDespues(indiceCar,vecCaracteristicas,text,maxVentana)
        if (cond):
            break
        else:
            cond,calificacion = buscarAntes(indiceCar,vecCaracteristicas,text,maxVentana)
            if(cond):
                break
    return calificacion

def buscarCalificaciones(vectorCaracteristicas,texto, maxVentana = 3):
    #Funcion que busque las relaciones entre las caracteristicas y sus calificaciones.
    
    #Vector de calificaciones a almacenar.
    vecCalificaciones = np.array([])
    
    for caracteristica in vectorCaracteristicas:
        #Buscar la calificacion.
        calif = buscarCalificacion(caracteristica,vectorCaracteristicas,texto,maxVentana)
        #Agregar la calificacion al vector,
        vecCalificaciones = np.append(vecCalificaciones,calif)
    return vectorCaracteristicas, vecCalificaciones    