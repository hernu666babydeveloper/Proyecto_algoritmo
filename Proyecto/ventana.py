
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QCheckBox, QGroupBox
import json



class mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,600,600)
        #self.setMaximumSize(30000,3000)
        #self.setMinimumSize(1200,1200)
        self.interfaz2()
        self.show()
    def interfaz2(self):
        # with open("G_resultado.json", "r")
        void= QLabel("")

        self.cajita1 = QGroupBox("Calculos de ICA")

        self.value1_ic = QLabel("v1")
        self.res1=  QLabel("s")
        self.unidad1 = QLabel("u1")

        
        self.value2_ic = QLabel("v2")
        self.res2=  QLabel("s")
        self.unidad2 = QLabel("u1")
        

        self.value3_ic = QLabel("v2")
        self.res3=  QLabel("s")
        self.unidad3 = QLabel("u1")


        self.value4_ic = QLabel("v2")
        self.res4=  QLabel("s")
        self.unidad4 = QLabel("u1")


        self.value5_ic = QLabel("v2")
        self.res5=  QLabel("s")
        self.unidad5 = QLabel("u1")


        self.value6_ic = QLabel("v2")
        self.res6=  QLabel("s")
        self.unidad6 = QLabel("u1")

        #layouts bacan bacan
        self.h_layout_1= QHBoxLayout()    
        self.h_layout_2= QHBoxLayout()    
        self.h_layout_3= QHBoxLayout()    

        #layouts unir 
        self.h_layout_1.addWidget(self.value1_ic)
        self.h_layout_1.addWidget(self.res1)
        self.h_layout_1.addWidget(self.unidad1)
        self.h_layout_1.addWidget(self.value2_ic)
        self.h_layout_1.addWidget(self.res2)
        self.h_layout_1.addWidget(self.unidad2)
        #layout 2
        self.h_layout_2.addWidget(self.value3_ic)
        self.h_layout_2.addWidget(self.res3)
        self.h_layout_2.addWidget(self.unidad3)
        self.h_layout_2.addWidget(self.value4_ic)
        self.h_layout_2.addWidget(self.res4)
        self.h_layout_2.addWidget(self.unidad4)
        #layout 3 
        self.h_layout_3.addWidget(self.value5_ic)
        self.h_layout_3.addWidget(self.res5)
        self.h_layout_3.addWidget(self.unidad5)
        self.h_layout_3.addWidget(self.value6_ic)
        self.h_layout_3.addWidget(self.res6)
        self.h_layout_3.addWidget(self.unidad6)
        #


    
        #
        self.v_layout= QVBoxLayout()
        self.biglayout= QVBoxLayout()
        self.v_layout.addLayout(self.h_layout_1) #cajita es  con set layout
        self.v_layout.addLayout(self.h_layout_2)
        self.v_layout.addLayout(self.h_layout_3)
        self.cajita1.setLayout(self.v_layout)
        self.cajita1.setFixedWidth(400)
        self.cajita1.move(0,400)
        #self.cajita1.setLayout(self.v_layout)
        self.biglayout.addWidget(self.cajita1)
        #self.biglayout.addWidget(void)
        self.biglayout.addWidget(void)
        self.setLayout(self.biglayout)