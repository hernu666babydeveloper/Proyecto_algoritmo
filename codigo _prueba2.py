import sys 
from PyQt6.QtWidgets import QApplication, QWidget

class venv(QWidget):

    def __init__(self):  #crea la ventana
        super().__init__()
        self.inicio() #metodo de funcion

    def inicio(self): #da los parameros de la ventana 
        self.setGeometry(100, 100, 250, 400) # Primer parametro x, y. ancho largo 
        self.setWindowTitle("ola querido") #nombre de ventana
        self.show(
        )

if __name__=="__main__":
    app=QApplication(sys.argv)#agregar desde  consola parametros
    ventana= venv(
    )
    sys.exit(app.exec())