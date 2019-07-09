# # DataUp
# Proyecto del curso "Taller de Proyecto". Análisis de entrevistas utilizando procesamiento de voz y técnicas de análisis de texto
#Programa principal.

#Imports.
from voz import *
from preProcesamiento import *
from busqueda import *
from visualizacion import *

def obtenerGrafico(tiempoEspera = 30):
    
    #Captura del audio
    try:
        texto = capturaAudio(tiempoEspera)
    except:
        print("Error en capturaAudio")
        return
    #Preprocesar Texto    
    try:
        text = preprocesar(texto)
    except:
        print("Error en text")
        return
    #Buscar caracteristicas y calificaciones.
    try:
        caracts, califs = buscarCalificaciones(['dulce','amargo','burbujas'],text,maxVentana = 3)
    except:
        print("Error en buscarCalificaciones")
        return
    #Grafico.
    try:
        visualizacion(caracts,califs)   
    except:
        print("Error en visualización")
        return
    
    return califs