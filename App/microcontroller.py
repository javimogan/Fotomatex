"""
    @javimogan - JAVIER ALONSO DIAZ
"""
from PyQt5 import QtCore


class Microcontroller(QtCore.QThread):
    emitSignal = QtCore.pyqtSignal(object)

    def __init__(self, _serial_connection, _interface_handler):
        QtCore.QThread.__init__(self)
        self.microcontroller = _serial_connection
        self.interface_handler = _interface_handler

    def run(self):
        while True:
            self.read_microcontroller()

    # Read data from the microcontroller
    def read_microcontroller(self):
        if self.microcontroller is not None:
            character = self.microcontroller.readline()
            if (character != b''):
                # Emit to take a photo
                self.emitSignal.emit('')
