"""
    @javimogan - JAVIER ALONSO DIAZ

    Interact with the camera

"""

import gphoto2 as gp

from PyQt5 import QtCore
import pyudev

import datetime
import os


class Camara(QtCore.QThread):
    emit_signal = QtCore.pyqtSignal(object)

    # Constructor
    def __init__(self, _gallery_path):
        QtCore.QThread.__init__(self)
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.camara = gp.check_result(gp.gp_camera_new())
        self.gallery_path = _gallery_path

    def run(self):
        print("CameraRun")
        if self.connect_camera():
            # Emit the signal
            print("\n\n Camera is connected \n\n")
            self.emit_signal.emit('')
        else:
            self.thread_connection()

    def set_gallery_path(self, _new_path):
        self.gallery_path = _new_path

    def connect_camera(self):
        try:
            gp.check_result(gp.gp_camera_init(self.camara))
            print(" ** Camera detected ** ")
            print(gp.check_result(gp.gp_camera_get_about(self.camara)))
            return True
        except gp.GPhoto2Error as ex:
            if ex.code == gp.GP_ERROR_MODEL_NOT_FOUND:
                print("Please, connect a camera")
            return False

    def thread_connection(self):
        self.monitor.filter_by(subsystem='usb')
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            if self.connect_camera():
                # Emit signal
                print("\n\n Camera is connected \n\n")
                self.emit_signal.emit('')
                return

    def take_photo(self):
        try:
            file_path = gp.check_result(gp.gp_camera_capture(self.camara, gp.GP_CAPTURE_IMAGE))

            hour = datetime.datetime.now()
            photo_name = "%s:%s:%s(%s).jpg" % (hour.hour, hour.minute, hour.second, hour.date())

            path = os.path.join(self.gallery_path, photo_name)

            # Take photo
            camera_file = gp.check_result(
                gp.gp_camera_file_get(self.camara, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))

            # Save the photo in the path
            gp.gp_file_save(camera_file, path)

            return True
        except gp.GPhoto2Error as ex:
            if ex.code == gp.GP_ERROR:
                print("An error occurred while taking the photo.")
                return False
