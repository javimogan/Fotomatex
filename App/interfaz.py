"""

    Manejo de la interfaz
    Actualizacion de foto
    Cuenta atras
    ...

"""

import glob
import os

from PyQt5 import QtCore
from PyQt5.QtCore import *


class manejoInterfaz:

    def __init__(self, _rutaFotos, _camara, _interfazArduino, _titulo, _cuenta, _img1, _img2, _img3, _img4,
                 _camaraControl, _botonControl):

        self.camaraControl = _camaraControl
        self.botonControl = _botonControl

        self.cuentaAtras = QtCore.QTimer()
        self.cuentaAtras.setInterval(1000)
        self.cuentaAtras.timeout.connect(self.displayTime)

        self.camara = _camara
        self.interfazArduino = _interfazArduino
        self.rutaFotos = _rutaFotos

        self.cuenta = _cuenta
        self.cuentaInicial = self.cuenta.property("text")

        self.titulo = _titulo
        self.textoInicial = self.titulo.property("text")

        self.img1 = _img1
        self.img2 = _img2
        self.img3 = _img3
        self.img4 = _img4
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def setRutaFotos(self, rutaNueva):
        self.rutaFotos = rutaNueva

    def cuentaAtrasStart(self):
        self.cuentaAtras.start()

    # Actualizar la foto de la pantalla
    def actualizarFoto(self):
        # Glob muestra los archivos de un directorio, los ordenamos por sorted
        # obtenemos la ruta de la imagen y la convertimos en string
        url2 = self.img2.property("source").toString()
        url3 = self.img3.property("source").toString()
        url4 = self.img4.property("source").toString()
        # Obtener la ultima foto subida
        list_of_files = glob.glob(os.path.join((self.rutaFotos), "*"))
        latest_file = max(list_of_files, key=os.path.getctime)

        urlUltima = QUrl.fromLocalFile(os.path.join(self.dir_path, latest_file))
        self.img1.setProperty("source", url2)
        self.img2.setProperty("source", url3)
        self.img3.setProperty("source", url4)
        self.img4.setProperty("source", urlUltima)

    # Mostrar o no la foto grande (Utilizado en la cuenta atras)
    def cambiarFotoVisible(self):
        if self.img4.property("visible"):
            self.img4.setProperty("visible", False)
        else:
            self.img4.setProperty("visible", True)

    # Cambiar el estado de los mensajes de camara y botonera no conectado
    def camaraVisible(self):
        self.camaraControl.setProperty("visible", False)

    def botonVisible(self):
        self.botonControl.setProperty("visible", False)

    # Poner en marcha la cuenta atras para realizar la foto
    def displayTime(self):
        mensajeAntesFoto = "PATATA"
        if (self.cuenta.property("text") == mensajeAntesFoto):
            self.cuentaAtras.stop()

            try:

                if (self.camara.hacerFoto()):
                    self.actualizarFoto()
            except:
                print("")
            finally:
                self.interfazArduino.escribirCaracter(b'c')

            self.cambiarFotoVisible()
            self.cuenta.setProperty("text", self.cuentaInicial)
            self.titulo.setProperty("text", self.textoInicial)
        elif (int(self.cuenta.property("text")) > 1):
            self.cuenta.setProperty("text", (int(self.cuenta.property("text")) - 1))
        elif (int(self.cuenta.property("text")) == 1):
            self.cuenta.setProperty("text", mensajeAntesFoto)

    # Hacer la Foto
    def hacerFoto(self):
        self.titulo.setProperty("text", "PREPÁRATE")
        self.cambiarFotoVisible()
        self.cuentaAtrasStart()
