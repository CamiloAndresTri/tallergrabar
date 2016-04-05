__author__ = 'miguelolivares'

from Seno import Seno
from archivar import Archivo
from Audiosystem import Audio


class metro:

    def __init__(Tempo,Metrica,Tono):
        self.Tempo = Tempo
        self.Metrica = Metrica
        self.Tono = Frecuencia

    def generar(self):
            wavearray = []
            for i in range(0, self.tamano):

                    datos = math.sin((2*math.pi*self.Frecuencia*i)/44100.0)

                    wavearray.append(datos)
            FinalData = np.asarray(wavearray)

            return FinalData

        print ("Generador de Onda Sinusoidal")
        Frecuenciadesampleo = 44100.0
        MaxBits = 16
        Buffer = 1024

        print ("Ingrese su opcion: ")
        Tono = input("Digite la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Level = input("Ingrese el valor pico de la senal en dBfs: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")

        onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)

        datos = onda.generar()
        datosAjustados = onda.leveladjust(datos,MaxBits,Level)
        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datosAjustados)

        Seleccion = raw_input("Desea reproducir el audio generado(si/no): ")

        if Seleccion == "si":
            audio = Audio(Buffer)
            Datos = audio.abrir(Nombre)
            audio.inicio(Datos[0],Datos[1],Datos[2])
            audio.reproducir(Datos[3])
            audio.cerrar()


if __name__ == "__main__":
    main()