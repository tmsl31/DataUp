# MODULO DE VOZ.

#Reconocimiento de voz.
import speech_recognition as sr
#import pyaudio
#Procesamiento de texto.
import re
#Procesamiento de lenguaje natural.
import nltk
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

def capturaAudio(tiempoEspera = 5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #Ajuste a piso de ruido.
        r.adjust_for_ambient_noise(source)
        print('Comience el audio (tiempo:' + str(tiempoEspera) + 'segundos)')
        #Iniciar escucha.
        audio = r.listen(source, timeout = tiempoEspera)
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            texto = r.recognize_google(audio,language="es-CL")
            print("Google Speech Recognition thinks you said " + texto)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print ('Termino de audio')
        
        return texto