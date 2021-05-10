#!/usr/bin/python3
"""
    Version 7.0

            * Comprueba la conexion con la botonera y la camra como thread independientes

"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

from camara import Camara
from interfaz import manejoInterfaz
from interfazArduino import InterfazArduino
from rutaFoto import Ruta
from variables import Variables


class Inicio:

    def __init__(self):
        self.rutaFotos = ''
        self.variablesGlobales = Variables()
        self.aplicacion = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.win = None
        self.iniciar()

        # Boton para cambiar ruta destino
        self.seleccionRuta = Ruta(self.rutaFotos)

        # 1 Comprobar que tenemos directorio para almacenar las fotos y preparar el click
        self.prepararRuta()
        self.rutaFotos = self.seleccionRuta.getRutaFotos()

        # 2 Conexion serial
        self.conexionSerie = InterfazArduino()
        self.conexionSerie.emitirArduinoConectado.connect(self.arduinoConectado)

        # 5 Camara
        self.camara = None
        self.camara = Camara(self.rutaFotos)
        self.camara.emitirSignal.connect(self.camaraConectada)

        # self.camara.conectarCamara()

        # 3 Clase manejo de la interfaz
        cuenta = self.win.findChild(QObject, "cuenta")
        self.titulo = self.win.findChild(QObject, "titulo")
        img1 = self.win.findChild(QObject, "imagen1")
        img2 = self.win.findChild(QObject, "imagen2")
        img3 = self.win.findChild(QObject, "imagen3")
        img4 = self.win.findChild(QObject, "imagen4")

        camaraControl = self.win.findChild(QObject, "controlCamara")
        botonControl = self.win.findChild(QObject, "controlBoton")

        self.manejoInterfaz = manejoInterfaz(self.rutaFotos, self.camara, self.conexionSerie, self.titulo, cuenta, img1,
                                             img2, img3, img4, camaraControl, botonControl)

        self.conexionSerie.emitirHacerFoto.connect(self.manejoInterfaz.hacerFoto)

        self.camara.start()
        self.conexionSerie.start()

        # FIN
        sys.exit(self.aplicacion.exec_())

    def camaraConectada(self):
        self.manejoInterfaz.camaraVisible()

    def arduinoConectado(self):
        self.manejoInterfaz.botonVisible()

    def iniciar(self):
        context = self.engine.rootContext()
        context.setContextProperty("main", self.engine)

        ruta = "%s%s" % (self.variablesGlobales.ruta, "./ui/main.qml")
        self.engine.load(ruta)
        self.win = self.engine.rootObjects()[0]
        self.win.show()

    def prepararRuta(self):
        # Comprobar si existe alguna ruta
        self.seleccionRuta.cambiarRutaFotos()
        self.win.findChild(QObject, "btnCambiarRuta").clicked.connect(self.setRutaFotos)

    def setRutaFotos(self):
        self.seleccionRuta.openFileNameDialog()
        self.rutaFotos = self.seleccionRuta.cambiarRutaFotos()
        self.camara.setRutaFotos(self.rutaFotos)
        self.manejoInterfaz.setRutaFotos(self.rutaFotos)


p = Inicio()
