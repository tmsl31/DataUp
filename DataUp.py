# # DataUp
# Proyecto del curso "Taller de Proyecto". Análisis de entrevistas utilizando procesamiento de voz y técnicas de análisis de texto
#Programa principal.

#Imports.
import voz
import preProcesamiento
import busqueda
import visualizacion


def obtenerGrafico(tiempoEspera = 10):
    #Captura del audio
    texto = voz.capturaAudio(tiempoEspera)
    #Preprocesar Texto
    text = preProcesamiento.preprocesar(texto)
    #Buscar caracteristicas y calificaciones.
    caracts,califs = busqueda.buscarCalificaciones(['dulce','amargo','burbujas'],text,maxVentana = 3)
    #Grafico.
    visualizacion.visualizacion(caracts,califs)

