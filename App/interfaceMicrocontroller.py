"""

    @javimogan - JAVIER ALONSO DIAZ

    Establish the serial connectionEstablish the serial connection
    and it is in charge of writing and reading of microcontroller

"""

import serial
import threading

from PyQt5 import QtCore
import pyudev

import serial.tools.list_ports


class InterfaceMicrocontroller(QtCore.QThread):
    emit_microcontrollerIsConnected = QtCore.pyqtSignal(object)
    emit_take_photo = QtCore.pyqtSignal(object)

    def __init__(self):
        QtCore.QThread.__init__(self)

        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.serial_connection = None

    def run(self):
        if self.connect_port():
            self.read_data()

        else:
            thread = threading.Thread(target=self.thread_connection)
            thread.daemon = True
            thread.start()

    def get_connection(self):
        return self.serial_connection

    # Connect to a port ant return True o False
    def connect_port(self):

        try:
            print("Connecting... ")
            i = 0
            connection_status = False
            while i < 10 and not connection_status:
                try:
                    #path = '/dev/ttyUSB' + str(i)
                    path = '/dev/ttyACM' + str(i)
                    # Open the port to 115200 baud
                    self.serial_connection = serial.Serial(path, 115200, timeout=1.0)
                    connection_status = True
                except:
                    connection_status = False
                    # print ("\t\t Error to connect the microcontroller in "+path)
                finally:
                    i = i + 1
            if connection_status:
                print("Connecting in " + path)
                return True
            else:
                print("Serial connection failure.")
                return False
        except:
            None

    # Write a character in a serial port
    def write_character(self, _char):
        print("Write character")
        if self.serial_connection is not None:
            self.serial_connection.write(_char)

    def thread_connection(self):
        self.monitor.filter_by(subsystem='usb')
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            if device.action == 'add':
                # some function to run on insertion of usb
                ports = list(serial.tools.list_ports.comports())
                for p in ports:
                    if "Microcontroller" in p[1]:
                        print("This is an Microcontroller!")
                        print(p)
                        if self.connect_port():
                            self.read_data()
                            # return

    def read_data(self):
        self.emit_microcontrollerIsConnected.emit('')
        while True:
            character = self.serial_connection.readline()
            if character != b'':
                # Emit to take a photo
                self.emit_take_photo.emit('')
