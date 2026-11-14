import sys 
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QCheckBox, QMessageBox, QGroupBox
from ventana import mainwin

import json

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
        self.ola = False
        self.inter()
        self.show()

    
      
    def inter(self):
       
       pmessage=  QLabel(" ingresa los datos")
       botton_crear = QPushButton("calcular ICA")
       botton_crear.clicked.connect(self.start_calwindow)
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
       #  """%, mg/L, mg/L, uS/cm, ph"""   
       #                      / input de valores
       value_1 = QLabel("OD")
       value_1.setFixedWidth(30)
       self.v1_input =  QLineEdit()
       value_1_unidad= QLabel("%") 
       value_1_unidad.setFixedWidth(30)

       value_2 =  QLabel("SST")
       value_2.setFixedWidth(30)
       self.v2_input = QLineEdit()
      
       value_2_unidad= QLabel(" mg/L")
       value_2_unidad.setFixedWidth(30)

       value_3 =  QLabel("DQO")
       value_3.setFixedWidth(30)
       self.v3_input = QLineEdit()
       value_3_unidad= QLabel(" mg/L")
       value_3_unidad.setFixedWidth(30)

       value_4 =  QLabel("CE")
       value_4.setFixedWidth(30)
       self.v4_input = QLineEdit()
       value_4_unidad= QLabel("uS/cm")
       value_4_unidad.setFixedWidth(30)

       value_5 =  QLabel("PH")
       value_5.setFixedWidth(30)
       self.v5_input = QLineEdit()
      
       value_5_unidad= QLabel("ph")
       value_5_unidad.setFixedWidth(30)

       value_6 =  QLabel("NT/NP")
       value_6.setFixedWidth(30)
       self.v6_input = QLineEdit()
       self.v6_input.setDisabled(True)
       value_6_unidad= QLabel("mg/l , mg/l")
       value_6_unidad.setFixedWidth(30)
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


        #boton 
        
    def true_v6(self, clicked): #
        if  clicked:
            self.v6_input.setDisabled(False) 
        else:
            self.v6_input.setDisabled(True)

    def start_calwindow (self):

        variables=[]
        
        variables_formulas=[]
        v1_listan = self.v1_input.text()
        v2_listan =self.v2_input.text() 
        v3_listan=self.v3_input.text()
        v4_listan =self.v4_input.text()
        v5_listan =self.v5_input.text()
        
        variables.append( v1_listan )
        variables.append( v2_listan )
        variables.append( v3_listan )
        variables.append( v4_listan )
        variables.append( v5_listan )
       
        #revisa si hay 6 variable
        if self.check_box.isChecked():
         v6_lista =self.v6_input.text()
         variables.append(v6_lista)
        else:
            v6_lista= 0
            

        #margen de error 
        a=1
        for i in variables:
            
            try: 
                a=a+1
                nuevalista= float(i)
                if abs(nuevalista) ==  nuevalista:
                    variables_formulas.append(nuevalista)     

                else: #uno nunca sabe el tontico que coloque -1, gracias santiago muac
                    QMessageBox.warning(self, "EHH", f"{i} no puede ser negativo \n ingrese denuevo el campo", 
                     QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

            except ValueError: 
                QMessageBox.warning(self, "error", f"{i} no es un numero \n ingrese de nuevo el campo ", 
                 QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                variables_formulas= []
                return
        #guardar en el json 

        if len(variables_formulas) == 5 or len(variables_formulas) == 6:
            try:
                with open("variables.json", "w") as file: #write, ruta del archivo
                    json.dump(variables_formulas, file)   #
            except FileNotFoundError as exept: #por si las moscas
                QMessageBox.warning(self, "error", "no se que paso lol",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close)


            #mensaje avisando que todo quedo bacan bacan
            QMessageBox.information(self, "Envio exitoso", "se han podido calcular los valores yupi",
            QMessageBox.StandardButton.Close,  QMessageBox.StandardButton.Close)

            #inicio otra ventana
            self.otraventana = mainwin()
            self.show()
           

# construnctor de ventana
if __name__ == "__main__":
    app= QApplication(sys.argv)
    wind  = M_win()
    print(wind.size()) #da el valor puesto en windsize
    sys.exit(app.exec())


