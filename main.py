# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import(QTime)

class MainWindow(QWidget):

   def __init__(self):
        super().__init__()

        self.createUI()

   def createUI(self):
        # This function don't call 'self.show()'

        # MainWindow setting
        self.setGeometry(300, 300, 400, 270)
        self.setFixedSize(400, 270)
        self.setWindowTitle('Timer')
        window_style = '''
            MainWindow{
                background-color: #151515;
            }
            '''
        self.setStyleSheet(window_style)

        # Create buttons
        self.btnR = QPushButton("Start", self)
        self.btnL = QPushButton("Cancel", self)

        # Create Label for display
        self.remaining_time = "00:00:00"
        self.lbl = QLabel(self.remaining_time, self) 
        lbl_style = '''
            QLabel{
                font-size: 90px; 
                color: #FAFAFA;
                font-family: Times;
                margin: 0px 0px 4px 0px;
            }
            '''
        self.lbl.setStyleSheet(lbl_style)

        # set layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnL)
        hbox.addStretch(1)
        hbox.addWidget(self.btnR)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())