
"""

    Nueva ventana para selccionar la ruta donde se almacenaran las fotos

"""

from PyQt5.QtWidgets import QWidget, QFileDialog

from variables import Variables

class Ruta(QWidget):
 
    def __init__(self, _rutaFotos):
        super().__init__()

        self.variablesGlobales = Variables()
        self.rutaArchivo = "%s%s" %(self.variablesGlobales.ruta,"ruta.txt")
        self.title = 'javimogan'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480


        self.rutaFotos = _rutaFotos

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
    def openFileNameDialog(self):
        fileName =QFileDialog.getExistingDirectory(self, '¿Dónde desea guardar las fotos?')
        f= open(self.rutaArchivo,"w+")
        f.write(fileName)
        f.close() 
        self.cambiarRutaFotos()
        
    def getRutaFotos(self):
        return self.rutaFotos

    def cambiarRutaFotos(self):
        
        f= open(self.rutaArchivo,"r+")
        
        self.rutaFotos = f.read()
        f.close() 
        if(self.rutaFotos == ''):
                self.openFileNameDialog()

        return self.rutaFotos