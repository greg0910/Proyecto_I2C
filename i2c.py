from tkinter import Button, Entry, Frame, Tk

ventana = Tk()
ventana.title("Proyecto_i2c")
ventana.geometry("400x300")
ventana.config(cursor="hand1")


#LEER LOS DATOS
#Panel para los datos
plano=Frame()
plano.place(width=200, height=300)
plano.config(bg="lightblue")
plano.config(bd=25)
plano.config(relief="sunken")



#BOTONES
#Boton leer voltaje
adc = Button(ventana, text="Leer el volatje",command="").place(x = 250,y = 20)


#Botones para encender y apagar el led
on = Button(ventana, text="Encender",command='').place(x = 250,y = 60)
off = Button(ventana, text="Apagar",command='').place(x = 320,y = 60)


#Botones para encender el led por segundo
seg = Button(ventana, text="Encender",command='').place(x = 320,y = 100)
tx2=Entry(ventana).place(x=250,y=100,width=60, height=30)


#Boton para las posiciones de la eeprom
rom = Button(ventana, text="Leer la Eeprom",command='').place(x = 250,y = 140)


#Boton para leer la posicion del bloque 2
rom2= Button(ventana, text="Leer el 2 bloque",command='').place(x = 250,y = 180)


#Boton para leer los datos de sensor
sen = Button(ventana, text="Datos del sensor",command='').place(x = 250,y = 220)


#Entrada texto para los comando
enter = Button(ventana, text="Enter",command='').place(x = 320,y = 260)
tx2=Entry(ventana).place(x=250,y=260,width=60, height=30)


ventana.mainloop()


