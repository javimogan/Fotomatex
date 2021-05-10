"""

    Establece la conexion serial 

    y es el encargado de escribir y leer de arduino

"""

import serial
import threading

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5 import QtCore
import pyudev

import serial.tools.list_ports



class InterfazArduino(QtCore.QThread):

    emitirArduinoConectado = QtCore.pyqtSignal(object)
    #emitirSignal = QtCore.pyqtSignal(object)
    emitirHacerFoto = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

        self.conexionSerie = None

            

    def run(self):
        if(self.conectarPuerto()):
            self.leerDatos()
            
        else:
            thread = threading.Thread(target=self.threadConexion)
            thread.daemon = True
            thread.start()

    def getConexion(self):
        return self.conexionSerie
    #Conectar a un puerto RETURN True o False
    def conectarPuerto(self):


        try:
            print("Conectando... ") 
            i = 0
            estadoConexion = False
            while (i<10 and not estadoConexion):	
                try:
                    ruta = '/dev/ttyACM'+str(i)
                    # Abrimos el puerto a 9600 baudios
                    self.conexionSerie = serial.Serial(ruta, 9600, timeout=1.0) 
                    estadoConexion = True
                except:
                    estadoConexion = False
                    #print ("\t\t Error al conectar Arduino en "+ruta)
                finally:
                    i = i+1
            if estadoConexion:
                print("Conectado en "+ruta)
                return True
            else:  
                print("Fallo en la conexion serie.")
                return False
        except:
            None
    
    #Escribir un caracter al puerto serie
    def escribirCaracter(self, car):
        print("escribir caracter")
        if(self.conexionSerie is not None):
            #b'c'
            self.conexionSerie.write(car)



    def threadConexion(self):
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            if device.action == 'add':
                # some function to run on insertion of usb
                ports = list(serial.tools.list_ports.comports())
                for p in ports:
                     if "Arduino" in p[1]:
                        print("This is an Arduino!")
                        print(p)
                        if(self.conectarPuerto()):
                            self.leerDatos()
                            #return
    def leerDatos(self):
        self.emitirArduinoConectado.emit('')
        while(True):
            caracter = self.conexionSerie.readline()
            if (caracter != b''):
                #Emitir para hacer la foto
                self.emitirHacerFoto.emit('')