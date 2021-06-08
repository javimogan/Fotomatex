"""
    @javimogan - JAVIER ALONSO DIAZ

"""

import os


class Variables():

    def __init__(self):
        os.chdir(os.path.dirname(__file__))
        self.ruta = os.getcwd() + "/"
