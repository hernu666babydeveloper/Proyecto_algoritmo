
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLineEdit, QCheckBox


class mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,600,600)
        #self.setMaximumSize(30000,3000)
        #self.setMinimumSize(1200,1200)
     
        self.show()

