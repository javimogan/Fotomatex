"""
    Esta clase es la encargada de interactuar con la camara

"""

# sudo apt-get install libgphoto2-dev
import os
class Variables():

    #Constructor
    def __init__(self):
        os.chdir(os.path.dirname(__file__))
        self.ruta = os.getcwd()+"/"
