
from  PyQt6.QtWidgets import QLabel, QDialog, QPushButton, QLineEdit, QMessageBox, QWidget
from PyQt6.QtGui import  QFont

class registro2(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ventana()
    def ventana(self):
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("registre su usuario")
        
        #no es necesaria volverla a abrir por eso se omite el shown
        user_label= QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont("Times New Roman",10))
        user_label.move(20,44)

        self.us_input= QLineEdit(self)
        self.us_input.resize(250,24)
        self.us_input.move(90,40)

        paws_label= QLabel(self)
        paws_label.setText("contraseña:")
        paws_label.setFont(QFont("Times New Roman",10))
        paws_label.move(20,90)

        self.pws_input= QLineEdit(self)
        self.pws_input.resize(250,24)
        self.pws_input.move(90,94)
        self.pws_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        paws2_label= QLabel(self)
        paws2_label.setText("Usuario:")
        paws2_label.setFont(QFont("Times New Roman",10))
        paws2_label.move(20,120)
        
        self.pws2_input= QLineEdit(self)
        self.pws2_input.resize(250,24)
        self.pws2_input.move(90,124)
        self.pws2_input.setEchoMode(
          QLineEdit.EchoMode.Password
                )

        create_push =  QPushButton(self)
        create_push.setText("Crear")
        create_push.resize(150,30)
        create_push.move(20,170)
        create_push.clicked.connect(self.Nuevousuario)

        cancel_push =  QPushButton(self)
        cancel_push.setText("Cerrar")
        cancel_push.resize(150,30)
        cancel_push.move(200,170)
        cancel_push.clicked.connect(self.cancelar)

    def cancelar(self):
        self.close()
    
    def Nuevousuario(self):
        pass   