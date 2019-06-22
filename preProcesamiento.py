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
#Desargar lista de stopwords.
nltk.download('stopwords')
nltk.download('wordnet')

#Definiciones de constantes.
#Sinonimos.
sinonimosDulce = ['dulce','dulzón', 'azucarado', 'acaramelado', 'dulcificado','dulzor']
sinonimosAmargo = ['amargo', 'agrio', 'aspero','amargor','agriedad','amargura']
sinonimosBurbujas = ['burbujas', 'burbujeo', 'efervescencia', 'espuma', 'efervescente', 'burbujeo', 'burbujear']
#Lista de stop words en espanol. Util para elminaras del texto original.
stopWords = set(stopwords.words("spanish"))

#Paso de texto a formato pandas.
def pasoPanda(texto):
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
    text = [word for word in text if not word in stopWords]
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

#Funcion de preprocesamiento.
def preprocesar(texto):
    #Paso a texto pandas.
    textoPandas = pasoPanda(texto)
    #Pre procesar.
    text = limpieza(textoPandas,stopWords)
    #Paso de numeros a enteros.
    text = text2int (text)
    #Quitar sinonimos
    text = homologarSinonimos(text)
    return text

