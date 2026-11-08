#qgirdlayput, poner un layout en cierta  cordenada cf en tipo celda

import sys
from  PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QTextEdit)


class m_win(QWidget):
    def __init__(self):
        super().__init__()
        self.inicio()
        #hacerla interactiva
        self.frst_val = ""
        self.scnd_val = "" 
        self.operador= ""
        self.pointer_flag = "1"
        self.aft_equal= False
        self.aft_oper= False

    def inicio(self):
        self.setGeometry(100,100,600,400)
        self.setMaximumSize(600, 400)
        self.setWindowTitle(" ")
        self.interfaz()
        self.show()

    def interfaz(self):
        self.pantalla = QTextEdit() #pantala modificable por eso el self
        self.pantalla.setDisabled(True) #Quitar la edicion de la cosa
        #botones numericos 
        boton_1= QPushButton("0") ; boton_1.clicked.connect(self.ing_datos)
        boton_2= QPushButton("1"); boton_2.clicked.connect(self.ing_datos)
        boton_3= QPushButton("2"); boton_3.clicked.connect(self.ing_datos)
        boton_4= QPushButton("3"); boton_4.clicked.connect(self.ing_datos)
        boton_5= QPushButton("4"); boton_5.clicked.connect(self.ing_datos)
        boton_6= QPushButton("5"); boton_6.clicked.connect(self.ing_datos)
        boton_7= QPushButton("6"); boton_7.clicked.connect(self.ing_datos)
        boton_8= QPushButton("7"); boton_8.clicked.connect(self.ing_datos)
        boton_9= QPushButton("8"); boton_9.clicked.connect(self.ing_datos)
        boton_10= QPushButton("9"); boton_10.clicked.connect(self.ing_datos)
        boton_pun= QPushButton(","); boton_pun.clicked.connect(self.ing_datos)
        boton_00= QPushButton("00"); boton_00.clicked.connect(self.ing_datos)

        #boton operacion 
        bott_sum= QPushButton("+") ;   bott_sum.clicked.connect(self.ins_opr)
        bott_res= QPushButton("-") ;   bott_res.clicked.connect(self.ins_opr)
        bott_div= QPushButton("/") ;   bott_div.clicked.connect(self.ins_opr)
        bott_mul= QPushButton("*") ;   bott_mul.clicked.connect(self.ins_opr)

        #botones de accion 
        bott_eliminartodo =  QPushButton("CE");   bott_mul.clicked.connect(self.borrartodo)
        bott_borrar= QPushButton ("<-");   bott_mul.clicked.connect(self.borraruno)
        bott_igual = QPushButton("=");   bott_mul.clicked.connect(self.igual)

        self.main_grid = QGridLayout()

        self.main_grid.addWidget(self.pantalla,0,0,2,4) #elemento / y,x  coordenadas donde inicia /expansion
        self.main_grid.addWidget(bott_eliminartodo,2,0,1,2)
        self.main_grid.addWidget(bott_borrar,2,2)
        self.main_grid.addWidget(bott_igual,2,3)
        #cordenad x= 0
        self.main_grid.addWidget(boton_2,3,0)
        self.main_grid.addWidget(boton_5,4,0)
        self.main_grid.addWidget(boton_8,5,0)
        self.main_grid.addWidget(boton_1,6,0)

        #cordenada x=1
        self.main_grid.addWidget(boton_3,3,1)
        self.main_grid.addWidget(boton_6,4,1)
        self.main_grid.addWidget(boton_9,5,1)
        self.main_grid.addWidget(boton_00,6,1)
        #coordenada x=2
        self.main_grid.addWidget(bott_igual,2,2)
        self.main_grid.addWidget(boton_4,3,2)
        self.main_grid.addWidget(boton_7,4,2)
        self.main_grid.addWidget(boton_10,5,2)
        self.main_grid.addWidget(boton_pun,6,2)
        #cordenada x=3
        self.main_grid.addWidget(bott_borrar,2,3)
        self.main_grid.addWidget(bott_div,3,3)
        self.main_grid.addWidget(bott_mul,4,3)
        self.main_grid.addWidget(bott_sum,5,3)
        self.main_grid.addWidget(bott_res,6,3)

        self.setLayout(self.main_grid)


    def  ing_datos(self):
        bott_text =self.sender().text()
        if self.pointer_flag == "1":
            self.frst_val += bott_text # self.frst_val= bott_text+seft.frst_val
            self.pantalla.setText(self.frst_val)
        else:
            self.scnd_val +=bott_text
            self.pantalla.setText(self.pantalla.toPlainText()+bott_text)

    def ins_opr(self):
        bott_text =self.sender().text()
        self.operador = bott_text
        self.pointer_flag="2"

        self.pantalla.setText(self.pantalla.toPlainText()+self.operador) 
        #toplaintext()devuelve el texto como ste
        #concatenar las strings para que se vean en pantalla , es el string de la pantalla 
        self.aft_oper=True


    def borrartodo(self):
        self.frst_val = ""
        self.scnd_val = "" 
        self.operador= ""
        self.pointer_flag = "1"
        self.aft_equal= False
        self.pantalla.setText("")
    def  borraruno(self):
        pass
    def igual(self):
        pass
if __name__ == "__main__" :
    app= QApplication(sys.argv)
    wndw = m_win() 
    sys.exit(app.exec())      