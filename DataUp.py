# # DataUp
# Proyecto del curso "Taller de Proyecto". Análisis de entrevistas utilizando procesamiento de voz y técnicas de análisis de texto
#Programa principal.

#Imports.
from voz import *
from preProcesamiento import *
from busqueda import *
from visualizacion import *

def procesarAudio(tiempoEspera = 30):
    
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
    
    return caracts, califs

def procesarAudioTest(tiempoEspera = 30):
    
    #Audio de prueba 
    texto = "dulce 1; amargo 3; gas 8"
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
    
    return caracts, califs

