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
    texto = capturaAudio(tiempoEspera)
    #Preprocesar Texto
    #texto = "El dulce estaba uno, el amargo un 8 y las burbujas un 10"
    #texto = "El dulce estaba uno, el amargo un 8 y las brujas un 10"
    text = preprocesar(texto)
    print(text)
    #Buscar caracteristicas y calificaciones.
    caracts,califs = buscarCalificaciones(['dulce','amargo','burbujas'],text,maxVentana = 3)
    #Grafico.
    visualizacion(caracts,califs)

