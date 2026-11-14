
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QCheckBox, QGroupBox, QMessageBox, QGridLayout, QDialog, QTextEdit
import json
import pyqtgraph as pg
import numpy as np
from Fun import Funciones


class mainwin(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,600,300)
        self.setMaximumSize(1200,900)
        self.setMinimumSize(600,300)
        
        #fuera del  Qwieget 
        self.setModal(True)
        self.funciones = Funciones()
        
        try:
            with open("G_resultado.json", "r") as archivo:
                self.lista=json.load(archivo)
        except FileNotFoundError:
            QMessageBox.warning(self, "QUE", "aparentemente no se guardo tu archivo sorry OwO",
            QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        
                 
        #Qwidger again
        self.interfaz2()
        self.show()


    def interfaz2(self):

        self.Grafica = self.grafica_lol()
        self.comnt =   self.comentarios_extra()
       
        """%, mg/L, mg/L, uS/cm, ph"""
        self.cajita1 = QGroupBox("Calculos de ICA")

        self.value1_ic = QLabel("OD")
        self.res1=  QLabel()
        self.res1.setText(str(self.lista[0]))
        self.unidad1 = QLabel("%")
      

        self.value2_ic = QLabel("SST")
        self.res2=  QLabel()
        self.res2.setText(str(self.lista[1]))
        self.unidad2 = QLabel("mg/L")
      
        

        self.value3_ic = QLabel("DQO")
        self.res3=  QLabel()
        self.res3.setText(str(self.lista[2]))
        self.unidad3 = QLabel(" mg/L")
      

        self.value4_ic = QLabel("CE")
        self.res4=  QLabel()
        self.res4.setText(str(self.lista[3]))
        self.unidad4 = QLabel("uS/cm")
        


        self.value5_ic = QLabel("PH")
        self.res5=  QLabel()
        self.res5.setText(str(self.lista[4]))
        self.unidad5 = QLabel("ph")


        self.value6_ic = QLabel("NT")
        self.res6=  QLabel()
        self.res6.setText(str(self.lista[5]))
        self.unidad6 = QLabel("mg/L/mg/L")
            
       
          
       

        #gridlayout
        self.gridlayout_1 = QGridLayout()
        self.gridlayout_1.addWidget(self.value1_ic,0,0)
        self.gridlayout_1.addWidget(self.value2_ic,1,0)
        self.gridlayout_1.addWidget(self.value3_ic,2,0)
        self.gridlayout_1.addWidget(self.value4_ic,3,0)
        self.gridlayout_1.addWidget(self.value5_ic,4,0)
        self.gridlayout_1.addWidget(self.value6_ic,5,0)

       
        self.gridlayout_1.addWidget(self.res1,0,1)
        self.gridlayout_1.addWidget(self.res2,1,1)
        self.gridlayout_1.addWidget(self.res3,2,1)
        self.gridlayout_1.addWidget(self.res4,3,1)
        self.gridlayout_1.addWidget(self.res5,4,1)
        self.gridlayout_1.addWidget(self.res6,5,1)

        self.gridlayout_1.addWidget(self.unidad1,0,2)
        self.gridlayout_1.addWidget(self.unidad2,1,2)
        self.gridlayout_1.addWidget(self.unidad3,2,2)
        self.gridlayout_1.addWidget(self.unidad4,3,2)
        self.gridlayout_1.addWidget(self.unidad5,4,2)
        self.gridlayout_1.addWidget(self.unidad6,5,2)
    
        #
        self.v_layout= QVBoxLayout()
        self.biglayout= QGridLayout()
        self.v_layout.addLayout(self.gridlayout_1) #cajita es  con set layout
        self.cajita1.setLayout(self.v_layout)
       
        
        #self.cajita1.setLayout(self.v_layout)
        self.biglayout.addWidget(self.cajita1,0,0,3,4)
        #self.biglayout.addWidget(void)
        self.biglayout.addWidget(self.Grafica,0,8,4,2)
        self.biglayout.addWidget(self.comnt,3,0,2,6)
        self.setLayout(self.biglayout)


    def grafica_lol(self):
        cosadelagrafica  =  pg.PlotWidget()
        x2 = np.arange(0,6)
        x = np.arange(0,5)
        y= self.lista[:5]
        if self.lista[5]!= 0:
            y= self.lista[:6]
            grafica1 = pg.BarGraphItem(x=x2, height = y, width = 0.5, brush ="#4B0082")
            
            cosadelagrafica.addItem(grafica1)
        else:
            y= self.lista[:5]
            grafica2 = pg.BarGraphItem(x=x, height= y, width = 0.5, brush ="#4B0082")
            cosadelagrafica.addItem(grafica2)
        cosadelagrafica.setWindowTitle("Grafica Variables  y subindices")
        cosadelagrafica.setDisabled(True)

        return cosadelagrafica #sin el return no funciona ola, no
    def comentarios_extra(self):
        comentarios_jij = QTextEdit()

        if self.lista[6] >=0.91:
            comentarios_jij.setText("el ICA es Bueno \n apto para habitad acuatico y otras actividades")
        elif self.lista[6] <=0.90 and self.lista[6] >=0.71:
            comentarios_jij.setText("el ICA es aceptable \n Es viable para el uso pero tiene ciertas alteraciones")
        elif self.lista[6] <=0.70 and self.lista[6] >=0.51:
            comentarios_jij.setText(" El ICA es Regular \n no se recomienda el uso de estas aguas, requieren tratamiento")
        elif self.lista[6] <=0.50 and self.lista[6] >=0.26:
            comentarios_jij.setText("El ICA es Malo \n no se recomienda el uso de estas aguas, requiere tratamiento urgente")
        elif self.lista[6] <=0.26 and self.lista[6] >=0:
            comentarios_jij.setText("El ICA es Muy malo \n La fuente está severamente contaminada y representa un riesgo para la salud y el ecosistema")
        comentarios_jij.setReadOnly(True)
        return comentarios_jij #sin return no creo que funcione