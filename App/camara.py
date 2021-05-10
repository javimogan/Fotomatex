"""
    Esta clase es la encargada de interactuar con la camara

"""

# sudo apt-get install libgphoto2-dev
import gphoto2 as gp


import serial
import threading

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5 import QtCore
import pyudev



import datetime, os

class Camara(QtCore.QThread):

    emitirSignal = QtCore.pyqtSignal(object)

    #Constructor
    def __init__(self, _rutaFotos):
        QtCore.QThread.__init__(self)
        self.camara = gp.check_result(gp.gp_camera_new())
        self.rutaFotos = _rutaFotos


    def run(self):
        print("Run de la camara")
        if(self.conectarCamara()):
            #Emitir señal
            print("\n\n Camara conectada \n\n")
            self.emitirSignal.emit('')
        else:
            """thread = threading.Thread(target=self.threadConexion)
            thread.daemon = True
            thread.start()"""
            self.threadConexion()


    def setRutaFotos(self, _rutaNueva):
        self.rutaFotos = _rutaNueva
    #Conexion con la camara
    def conectarCamara(self):
        mensaje = True
        try:
            # gphoto2 version 2.5+
            gp.check_result(gp.gp_camera_init(self.camara))
                #Aqui la camara ya esta conectada e identificada
            #Mostramos la informacion de la camara
            print(" ** Camara detectada ** ")
            print(gp.check_result(gp.gp_camera_get_about(self.camara)))
            return True
        except gp.GPhoto2Error as ex:
            if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND and mensaje:
                print("Por favor, conecte una cámara")
                mensaje = False
            return False
       


    def threadConexion(self):
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            if(self.conectarCamara()):
                #Emitir señal
                print("\n\n Camara conectada \n\n")
                self.emitirSignal.emit('')
                return

    def hacerFoto(self):
        try:
            file_path = gp.check_result(gp.gp_camera_capture(self.camara, gp.GP_CAPTURE_IMAGE))

            #Damos el nombre a la foto con la Hora-minuto-Segundo-Fecha
            hora = datetime.datetime.now()
            nombreFoto = "%s:%s:%s(%s).jpg" %(hora.hour, hora.minute, hora.second,hora.date())
            
            #Ruta donde se almacenara la foto
            ruta = os.path.join(self.rutaFotos, nombreFoto)
            #print(ruta)
            #print(self.rutaFotos)
            #Capturar foto
            camera_file = gp.check_result(gp.gp_camera_file_get(self.camara, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
            
            #Guardar la foto en la ruta
            gp.gp_file_save(camera_file, ruta)

            return True
        except gp.GPhoto2Error as ex:
                if ex.code == gp.GP_ERROR:
                        print("Ha ocurrido un error al realizar la foto.")
                        return False

        
