#Modulo de preprocesamiento.

#Imports.
import numpy as np
import pandas as pd
#Procesamiento de lenguaje natural.
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
#Busqueda de diferencias entre palabras.
from jiwer import wer
#Desargar lista de stopwords.
nltk.download('stopwords')
nltk.download('wordnet')
import re

#Definiciones de constantes.
#Caracteristicas.
caractsBuscar = ['dulce','amargo','burbujas']
#Sinonimos.
sinonimosDulce = ['dulce','dulzón', 'endulces' , 'azucarado', 'acaramelado', 'dulcificado','dulzor']
sinonimosAmargo = ['amargo', 'agrio', 'aspero','amargor','agriedad','amargura']
sinonimosBurbujas = ['burbujas', 'burbujeo', 'efervescencia', 'espuma', 'efervescente', 'burbujeo', 'burbujear','gas']
#Lista de stop words en espanol. Util para elminaras del texto original.
stopWords = set(stopwords.words("spanish"))


#Paso de texto a formato pandas.
def pasoPanda(texto):
    print('Paso a pandas')
	#Funcion que pase el texto a formato Pandas. Solo para preproesar.
    output = pd.DataFrame([texto],columns = ['Texto'], index = [1])
    return output

#Paso del texto  a vector de strings.
def limpieza(textoPandas,stopWords, deleteStopWords = 1, lemanizar= 0):
    #Funcion que realiza el preProcesamiento del texto.
    #Convertir a Pandas.
    text = textoPandas['Texto'][1]
    #Pasar a minusculas.
    text = text.lower()
    #Eliminar comas y simbolos.
    text = re.sub(r'[^\w\s]','',text)
    #Convertir a vector de palabras.
    text = text.split()
    #Eliminar stopWords
    #text = [word for word in text if not word in stopWords]
    text = [word for word in text if (1==1)]
    #Decidir si lemanizar o no
    if lemanizar == 1:
        lem = WordNetLemmatizer()
        text = np.array([lem.lemmatize(word) for word in text])
    elif lemanizar == 2:
        stem = PorterStemmer()
        text = np.array([stem.stem(word) for word in text])
    return text


#Paso de numeros en palabras a numeros.
def text2int (textnum, numwords={}):
    if not numwords:
        units = [
        "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
        "nueve", "diez", "once", "doce"]

        diccionario = {units[0]:0,units[1]:1,units[2]:2,units[3]:3,units[4]:4,units[5]:5, units[6]:6, units[7]:7,units[8]:8,units[9]:9,units[10]:10,units[11]:11,units[12]:12}
    
    copiaTextNum = textnum;
    count = 0
    for word in copiaTextNum:
        if word not in units:
            count += 1
        else:
            copiaTextNum[count] = str(diccionario[word]);
            count += 1            
    return copiaTextNum

#Funciones para trabajos sobre sinonimos.
def homologarSinonimosUnaPalabra(vectorTexto,sinonimos):
    #Numero de palabras de la grabación.
    numeroPalabras = len(vectorTexto)
    #Casos para cada palabra
    count = 0
    while count < numeroPalabras:
        if vectorTexto[count] in sinonimos:
            vectorTexto[count] = sinonimos[0]
        count += 1
    return vectorTexto    

def homologarSinonimos(texto):
    #Metodo que realice el cambio de palabras para las caracteristicas de interes.
    texto = homologarSinonimosUnaPalabra(texto,sinonimosDulce)
    texto = homologarSinonimosUnaPalabra(texto,sinonimosAmargo)
    texto = homologarSinonimosUnaPalabra(texto,sinonimosBurbujas)
    return texto

#Cambio de palabras a la palabra mas cercana dentro de las caracteristicas
def reemplazoPalabraCercana(caracteristica,texto):
	#Funcion que busque las diferencias entre palabras
	#Se utiliza como metrica la distancia de Levenshtein.

    #Vector que almacene la distancia de las palabras de la frase.
    distancias = np.array([])
    #Recorrer texto buscando
    count = 0
    for palabra in texto:
        #Calcular la distancia.
        distancia = nltk.edit_distance(caracteristica,palabra)
        #Anexar la distancias.
        distancias = np.append(distancias,distancia);
    #Buscar la posición de la minima distancia.
    argminDistancia = np.argmin(distancias)
    #Reemplazar esta palabra por la caracteristica que falta.
    print(argminDistancia)
    texto[argminDistancia] = caracteristica;
    return texto

def reemplazoPalabrasCercanas(caracteristicas,texto):
	#Funcion que realice el reemplazo de todas las palabras del vector de caractericas.

    #Indices de las caracteristicas.
    estar = np.array([])
    for caract in caracteristicas:
        #Indices de ocurrencia.
        indice = np.where(texto == caract)
        #Obtener el largo de los indices.
        nIndices = np.shape(indice)[1]
        if (nIndices == 0):
            #Caso en que la caracteristica no esta en la frase.
            estar = np.append(estar,0)
            #Caso en que la caracteristica esta en la frase.
        else:
            estar = np.append(estar,1)
    #Obtener las caracteristicas que faltan en la frase analizada.
    faltan = np.array([])
    count = 0
    # Mantener las que faltan
    for caract in caracteristicas:
        if (estar[count] == 0):
            faltan = np.append(faltan,caract)
        count += 1
    # Buscar el reemplazo para las palabras que faltan.
    for caract in faltan:
        texto = reemplazoPalabraCercana(caract,texto)
    return texto


#Funcion de preprocesamiento.
def preprocesar(texto):
    #Paso a texto pandas.
    textoPandas = pasoPanda(texto)
    #Pre procesar.
    text = limpieza(textoPandas,stopWords)
    #paso a numpy
    text = np.array(text)
    text = text.astype('U256') 
    #Paso de numeros a enteros.
    text = text2int (text)
    #Quitar sinonimos
    text = homologarSinonimos(text)
    #Cambiar palabras cercanas a las caracteristicas.
    reemplazoPalabrasCercanas(caractsBuscar,text)
    return text


