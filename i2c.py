from cProfile import label
from cgitb import text
from tkinter import Button, Entry, Frame, Label, Scrollbar, Tk
import tkinter
import serial

#Ventana Principal
ventana = Tk()
ventana.title("Proyecto_i2c")
ventana.geometry("400x300")
ventana.config(cursor="hand1")
#Cuadro
plano=Frame()
plano.place(width=400, height=300)
plano.config(bg="lightblue")
plano.config(bd=25)
plano.config(relief="sunken")


#Variables


def dat():
    Nucleo = serial.Serial('COM10', 9600)
    while True:
     rawString = str(Nucleo.readline())
     rawString = rawString.strip("b'\.n")  # Ya tengo mi valor @num# limpio
    # Se verifica la trama
     if (rawString.count('@') == 1) and (rawString.count('#') == 1):
        sensor = float(rawString.strip("@#"))
        
  

#LEER LOS DATOS

scroll=Scrollbar(ventana)


#BOTONES
#Boton leer voltaje
adc = Button(ventana, text="Leer el volatje",command="Datos").place(x = 250,y = 40)


#Botones para encender y apagar el led
on = Button(ventana, text="Encender",command='').place(x = 250,y = 80)
off = Button(ventana, text="Apagar",command='').place(x = 320,y = 80)

#Boton para las posiciones de la eeprom
rom = Button(ventana, text="Leer la Eeprom",command='').place(x = 250,y = 120)


#Boton para leer la posicion del bloque 2
rom2= Button(ventana, text="Leer el 2 bloque",command='').place(x = 250,y = 160)


#Boton para leer los datos de sensor
sen = Button(ventana, text="Datos del sensor",command='').place(x = 250,y = 200)


#Entrada texto para los comando
enter = Button(ventana, text="Enter",command='').place(x = 320,y =240)
tx2=Entry(ventana).place(x=250,y=240,width=60, height=30)


ventana.mainloop()





