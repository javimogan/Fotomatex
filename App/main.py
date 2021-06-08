#!/usr/bin/python3
"""
    Version 7.0
"""

import sys

from PyQt5.QtCore import *
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

from camara import Camara
from interfaz import InterfaceHandler
from interfaceMicrocontroller import InterfaceMicrocontroller
from rutaFoto import GalleryPath
from variables import Variables


class Fotomatex:

    def __init__(self):
        self.path_gallery = ''
        self.global_variables = Variables()
        self.application = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.win = None
        self.start()

        self.select_gallery_path = GalleryPath(self.path_gallery)

        # 1 Check that we have a directory to store the photos and prepare the click
        self.prepare_path()
        self.path_gallery = self.select_gallery_path.get_gallery_path()

        # 2 Serial connection
        self.serial_connection = InterfaceMicrocontroller()
        self.serial_connection.emit_microcontrollerIsConnected.connect(self.microcontroller_is_connected)

        # 3 Camera
        self.camera = None
        self.camera = Camara(self.path_gallery)
        self.camera.emit_signal.connect(self.camera_is_connected)


        # 4 Interface handling
        counter = self.win.findChild(QObject, "counter")
        self.title = self.win.findChild(QObject, "title")
        img1 = self.win.findChild(QObject, "imagen1")
        img2 = self.win.findChild(QObject, "imagen2")
        img3 = self.win.findChild(QObject, "imagen3")
        img4 = self.win.findChild(QObject, "imagen4")

        camera_control = self.win.findChild(QObject, "controlCamara")
        button_control = self.win.findChild(QObject, "controlBoton")

        self.interface_handler = InterfaceHandler(self.path_gallery, self.camera, self.serial_connection, self.title,
                                                  counter, img1, img2, img3, img4, camera_control, button_control)

        self.serial_connection.emit_take_photo.connect(self.interface_handler.take_photo)

        self.camera.start()
        self.serial_connection.start()

        # END
        sys.exit(self.application.exec_())

    def camera_is_connected(self):
        self.interface_handler.visible_camera()

    def microcontroller_is_connected(self):
        self.interface_handler.visible_button()

    def start(self):
        context = self.engine.rootContext()
        context.setContextProperty("main", self.engine)

        ruta = "%s%s" % (self.global_variables.ruta, "./ui/main.qml")
        self.engine.load(ruta)
        self.win = self.engine.rootObjects()[0]
        self.win.show()

    def prepare_path(self):
        self.select_gallery_path.change_gallery_path()
        self.win.findChild(QObject, "btnCambiarRuta").clicked.connect(self.set_gallery_path)

    def set_gallery_path(self):
        self.select_gallery_path.open_file_name_dialog()
        self.path_gallery = self.select_gallery_path.change_gallery_path()
        self.camera.set_gallery_path(self.path_gallery)
        self.interface_handler.set_gallery_path(self.path_gallery)


p = Fotomatex()
