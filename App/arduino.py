
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5 import QtCore


class Arduino(QtCore.QThread):

    emitirSignal = QtCore.pyqtSignal(object)

    def __init__(self, _conexionSerie, _manejoInterfaz):
        QtCore.QThread.__init__(self)
        self.arduino = _conexionSerie
        self.manejoInterfaz = _manejoInterfaz

    def run(self):
        while(True):
            self.leerArduino()

    #Leer datos del arduino
    def leerArduino(self):
        if(self.arduino is not None):
            caracter = self.arduino.readline()
            if (caracter != b''):
                #Emitir para hacer la foto
                self.emitirSignal.emit('')
