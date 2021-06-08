"""
    @javimogan - JAVIER ALONSO DIAZ

    New windows to select the path where the images are stored

"""

from PyQt5.QtWidgets import QWidget, QFileDialog

from variables import Variables


class GalleryPath(QWidget):

    def __init__(self, _gallery_path):
        super().__init__()

        self.global_variables = Variables()
        self.path_file = "%s%s" % (self.global_variables.ruta, "path.txt")
        self.title = 'javimogan'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.gallery_path = _gallery_path

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def open_file_name_dialog(self):
        file_name = QFileDialog.getExistingDirectory(self, '¿Dónde desea guardar las fotos?')
        f = open(self.path_file, "w+")
        f.write(file_name)
        f.close()
        self.change_gallery_path()

    def get_gallery_path(self):
        return self.gallery_path

    def change_gallery_path(self):
        f = open(self.path_file, "r+")

        self.gallery_path = f.read()
        f.close()
        if self.gallery_path == '':
            self.open_file_name_dialog()

        return self.gallery_path
