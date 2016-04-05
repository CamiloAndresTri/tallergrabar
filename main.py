__author__ = 'miguelolivares'



from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from grabar import Grabar
import pyaudio





def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")

    audio1 = Grabar(CHUNK, FORMAT, CHANNELS, RATE)


    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    global arreglo1

    arreglo1 = []


    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)


    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame1, fg="black", padx=15, pady=10, text="Digite el nombre del archivo 1:")
    cuadro.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 1.

    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=15, pady=10)

    # Creacion e insercion del cuadro de texto 2.

    cuadro2= Label(frame1, fg="black", padx=15, pady=10, text="Digite el Tempo del metronomo:")
    cuadro2.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 2.

    e2 = Entry(frame1, bd=5, insertwidth=1)
    e2.pack(side=LEFT, padx=15, pady=5)

    # Creacion e insercion del cuadro de texto 3.

    cuadro3= Label(frame1, fg="black", padx=15, pady=10, text="Digite la metrica del metronomo:")
    cuadro3.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 3.

    e3 = Entry(frame1, bd=5, insertwidth=1)
    e3.pack(side=LEFT, padx=15, pady=5)

    # Creacion e insercion del cuadro de texto 4.

    cuadro4= Label(frame1, fg="black", padx=15, pady=10, text="Digite el tono del metronomo:")
    cuadro4.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 4.

    e4 = Entry(frame1, bd=5, insertwidth=1)
    e4.pack(side=LEFT, padx=15, pady=5)


    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...')

    # Funcion activa mensaje y grabar

    def activasms1():
        if (e1.get()) & (e2.get()) & (e3.get()) & (e4.get()) == '':
            print 'error'
            tkMessageBox._show('Error', 'Asegurese de ingresar bien los datos.')
        else:
            d.set(True)
            e1.configure(state='disabled')
            e2.configure(state='disabled')
            e3.configure(state='disabled')
            e4.configure(state='disabled')
            audio1.inicio()
            mensaje1.pack(side=LEFT)
            while d.get():
                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break



    # Funcion desactiva mensaje y para de grabar.
    def desactivasms1():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        global  arreglo1
        arreglo1 = audio1.parar()

        audio1.creaAudio(e1.get())
        grabarButton1.pack_forget()
        pararButton1.pack_forget()





    def reproduccion1():
        audio1.reproduce(e1.get())



    # Creacion de botones.
    grabarButton1 = Button(frame2, padx=30, pady=2, text="Grabar", command=activasms1)
    grabarButton1.pack(side=LEFT)

    pararButton1 = Button(frame2, padx=30, pady=2, text="Parar", command=desactivasms1)
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame2, padx=20,pady=2, text="Reproducir", command=reproduccion1)
    reproducirButton1.pack(side=RIGHT)



    ventana.mainloop()

if __name__ == "__main__":
    main()