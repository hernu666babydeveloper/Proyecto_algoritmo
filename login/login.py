import sys 
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap
from registro import registro2
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
        self.pasw_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.check_view_pasw = QCheckBox(self)
        self.check_view_pasw.setText("mostras contraseña")
        self.check_view_pasw.move(90,110)
        self.check_view_pasw.toggled.connect(self.showpasw)

        iniboton=QPushButton(self)
        iniboton.setText("login")
        iniboton.resize(320,24)
        iniboton.move(20,180)
        iniboton.clicked.connect(self.startmainview)

        regiboton=QPushButton(self)
        regiboton.setText("Registrar")
        regiboton.resize(320,24)
        regiboton.move(20,140)
        regiboton.clicked.connect(self.registro)
    #SIGNAL AND SLOTS 
    def showpasw(self, clicked):
        if clicked:
            self.pasw_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.pasw_input.setEchoMode(
              QLineEdit.EchoMode.Password
               )
    
    def startmainview(self):
        pass
    def  registro(self):
       self.new_user= registro2()
       self.new_user.show()









if __name__=="__main__":
    app= QApplication(sys.argv)
    login = inicio()
    sys.exit(app.exec())

