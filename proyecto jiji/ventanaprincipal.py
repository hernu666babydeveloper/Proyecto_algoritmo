import sys 
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QCheckBox


class M_win(QWidget):
    def __init__(self):
        super().__init__()
        self.inicio()
    def inicio(self):
        self.setGeometry(100,100,300,300)
        self.setMaximumSize(300, 300)
        self.setMinimumSize(300, 300)
        self.setWindowTitle("")
        self.bool_1 = True
        self.inter()
        self.show()
    
      
    def inter(self):
       pmessage=  QLabel(" ingresa los datos")
       botton_crear = QPushButton("calcular ICA")
                 #ek comando size sale error, solo es para ver el valor
        #espacios vacios
       void= QLabel("")
       void1= QLabel("")
       void2= QLabel("")
       void3= QLabel("")
       void4= QLabel("")
       void5= QLabel("")
       void6 = QLabel("")
       #valores mostrados            
       #                      / input de valores
       value_1 = QLabel("V1")
       self.v1_input =  QLineEdit()
       value_1_unidad= QLabel("un")

       value_2 =  QLabel("V2")
       self.v2_input = QLineEdit()
       value_2_unidad= QLabel("un")

       value_3 =  QLabel("V3")
       self.v3_input = QLineEdit()
       value_3_unidad= QLabel("un")

       value_4 =  QLabel(" V4")
       self.v4_input = QLineEdit()
       value_4_unidad= QLabel("un")

       value_5 =  QLabel("V5")
       self.v5_input = QLineEdit()
       value_5_unidad= QLabel("un")

       value_6 =  QLabel("V6")
       self.v6_input = QLineEdit()
       self.v6_input.setDisabled(True)
       value_6_unidad= QLabel("un")
       #checkbot 
       self.check_box= QCheckBox("¿hay v6?",self)
       self.check_box.clicked.connect(self.true_v6)
       
   
       #layaout h
       self.h_layout_1= QHBoxLayout()    
       self.h_layout_2= QHBoxLayout()    
       self.h_layout_3= QHBoxLayout()    
       self.h_boton_layout =  QHBoxLayout()
       self.h_check_box_layout = QHBoxLayout()
       #anidar los layauts
       self.h_layout_1.addWidget(value_1)
       self.h_layout_1.addWidget(self.v1_input)
       self.h_layout_1.addWidget(value_1_unidad)
       self.h_layout_1.addWidget(value_2)
       self.h_layout_1.addWidget(self.v2_input)
       self.h_layout_1.addWidget(value_2_unidad)
       #layout dos
       self.h_layout_2.addWidget(value_3)
       self.h_layout_2.addWidget(self.v3_input)
       self.h_layout_2.addWidget(value_3_unidad)
       self.h_layout_2.addWidget(value_4)
       self.h_layout_2.addWidget(self.v4_input)
       self.h_layout_2.addWidget(value_4_unidad)
      
       #layoit tres
       self.h_layout_3.addWidget(value_5) #1
       self.h_layout_3.addWidget(self.v5_input)#2
       self.h_layout_3.addWidget(value_5_unidad)#3
       self.h_layout_3.addWidget(value_6)#4
       self.h_layout_3.addWidget(self.v6_input)#5
       self.h_layout_3.addWidget(value_6_unidad)#6
       #layoutboton
       self.h_boton_layout.addWidget(void1)
       self.h_boton_layout.addWidget(botton_crear)
       self.h_boton_layout.addWidget(void2)
       #layoutcheckbox
       self.h_check_box_layout.addWidget(void3)
       self.h_check_box_layout.addWidget(void4)
       self.h_check_box_layout.addWidget(void6)
       self.h_check_box_layout.addWidget(self.check_box)
       self.h_check_box_layout.addWidget(void5)
       #anidar
       self.vp_layout=  QVBoxLayout()

       self.vp_layout.addWidget(pmessage)
       self.vp_layout.addLayout(self.h_layout_1)
       self.vp_layout.addLayout(self.h_layout_2)
       self.vp_layout.addLayout(self.h_layout_3)
       self.vp_layout.addLayout(self.h_check_box_layout)
       
       self.vp_layout.addWidget(void)
       
       self.vp_layout.addLayout(self.h_boton_layout)
       self.setLayout(self.vp_layout)

    def true_v6(self, clicked): #
        if  clicked:
            self.v6_input.setDisabled(False)
            
        else:
            self.v6_input.setDisabled(True)
            self.v6_input = None


      
      



# construnctor de ventana
if __name__ == "__main__":
    app= QApplication(sys.argv)
    wind  = M_win()
    print(wind.size()) #da el valor puesto en windsize
    sys.exit(app.exec())


