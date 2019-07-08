#nterfaz del proyecto DataUp.

#Imports.
from DataUp import *
from tkinter import Tk, Label, Button
from tkinter import *
from tkinter.ttk import *

#Generar ventana de tkinter.
root = Tk() 

# Adding widgets to the root window 
Label(root, text = 'DataUp', font =('Verdana', 15)).pack(side = TOP, pady = 10) 

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\Users\tlara\OneDrive\Documentos\GitHub\DataUp\microphone.png") 

# Resizing image to fit on button 
photoimage = photo.subsample(5, 5) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
Button(root, text = 'Grabar!', image = photoimage, compound = LEFT).pack(side = TOP) 

mainloop() 
