import sys 
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap
class inicio(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciarui()

    def iniciarui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("iniciarsesionlolcf")
        self.generarelcosodeinicio()
        self.show()
    def generarelcosodeinicio(self):
        self.is_logged = False
        #muestra txt
        user_label = QLabel(self) 
        user_label.setText("usuario:")
        user_label.setFont(QFont("Times New Roman", 10))
        user_label.move(20,54)

        #donde colocas txt
        self.usr_input = QLineEdit(self)
        self.usr_input.resize(250,24) #ancho y alto 
        self.usr_input.move(90,50)

        pasw_label = QLabel(self) 
        pasw_label.setText("Contraseña:")
        pasw_label.setFont(QFont("Times New Roman", 10))
        pasw_label.move(20,84)

        self.pasw_input = QLineEdit(self)
        self.pasw_input.resize(250,24) #ancho y alto 
        self.pasw_input.move(90,84)
        
if __name__=="__main__":
    app= QApplication(sys.argv)
    login= inicio()
    sys.exit(app.exec())

