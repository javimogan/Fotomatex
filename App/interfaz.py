"""
    @javimogan - JAVIER ALONSO DIAZ

    Interface management
    Update the photo
    CountDown
    ...

"""

import glob
import os

from PyQt5 import QtCore
from PyQt5.QtCore import *


class InterfaceHandler:

    def __init__(self, _gallery_path, _camera, _arduino_interface, _title, _counter, _img1, _img2, _img3, _img4,
                 _camera_control, _button_control):

        self.camera_control = _camera_control
        self.buttonControl = _button_control

        self.count_down = QtCore.QTimer()
        self.count_down.setInterval(1000)
        self.count_down.timeout.connect(self.display_time)

        self.camera = _camera
        self.arduino_interface = _arduino_interface
        self.gallery_path = _gallery_path

        self.counter = _counter
        self.initial_counter = self.counter.property("text")

        self.title = _title
        self.initial_text = self.title.property("text")

        self.img1 = _img1
        self.img2 = _img2
        self.img3 = _img3
        self.img4 = _img4
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def set_gallery_path(self, _newPath):
        self.gallery_path = _newPath

    def start_count_down(self):
        self.count_down.start()

    def update_photo(self):
        url2 = self.img2.property("source").toString()
        url3 = self.img3.property("source").toString()
        url4 = self.img4.property("source").toString()
        list_of_files = glob.glob(os.path.join(self.gallery_path, "*"))
        latest_file = max(list_of_files, key=os.path.getctime)

        latest_url = QUrl.fromLocalFile(os.path.join(self.dir_path, latest_file))
        self.img1.setProperty("source", url2)
        self.img2.setProperty("source", url3)
        self.img3.setProperty("source", url4)
        self.img4.setProperty("source", latest_url)

    def change_visible_photo(self):
        if self.img4.property("visible"):
            self.img4.setProperty("visible", False)
        else:
            self.img4.setProperty("visible", True)

    def visible_camera(self):
        self.camera_control.setProperty("visible", False)

    def visible_button(self):
        self.buttonControl.setProperty("visible", False)

    # Start countdown to take photo
    def display_time(self):
        message_before_photo = "PATATA"
        if self.counter.property("text") == message_before_photo:
            self.count_down.stop()

            try:
                if self.camera.take_photo():
                    self.update_photo()
            except:
                print("")
            finally:
                self.arduino_interface.write_character(b'c')

            self.change_visible_photo()
            self.counter.setProperty("text", self.initial_counter)
            self.title.setProperty("text", self.initial_text)
        elif int(self.counter.property("text")) > 1:
            self.counter.setProperty("text", (int(self.counter.property("text")) - 1))
        elif int(self.counter.property("text")) == 1:
            self.counter.setProperty("text", message_before_photo)

    # Take photo
    def take_photo(self):
        self.title.setProperty("text", "PREPÁRATE")
        self.change_visible_photo()
        self.start_count_down()
