# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QTimeEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (QTime, pyqtSignal)
from PyQt5.QtGui import (QIcon)
class InputWindow(QWidget):

    valueChanged = pyqtSignal(QTime)

    def __init__(self):
        super().__init__()

        self.time = QTime(0,0,0,0)

        self.createUI()
        self.connectSignal()

    def createUI(self):
         # This function don't call 'self.show()'

        # MainWindow setting
        self.setGeometry(300, 300, 230, 130)
        self.setFixedSize(230, 130)
        self.setWindowTitle('InputWindow')
        self.setWindowIcon(QIcon('Resources/kitchen_timer.png'))
        window_style = '''
            InputWindow{
                background-color: #48DA04;
            }
            '''
        self.setStyleSheet(window_style)

        # create Label
        self.lbl = QLabel("Plase set the time")  
        lbl_style = '''
            QLabel{
                font-size: 20px; 
                color: #FFFFFF;
                font-family: Times;
            }
            '''
        self.lbl.setStyleSheet(lbl_style)

        # create TimeEdit
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm:ss")
        time_edit_style = '''
            QTimeEdit{
                font-family: Times;
            }
            '''
        self.time_edit.setStyleSheet(time_edit_style)    

        # create Botton
        self.btnR = QPushButton("Determine", self)
        self.btnL = QPushButton("Cansel", self)
        self.btnR.setFixedSize(90, 20)
        self.btnL.setFixedSize(90, 20)
        btn_style = '''
            QPushButton{
                color: #090909;
                font-family: Times;
                background-color: #FAED02;
            }
            '''
        self.btnR.setStyleSheet(btn_style)
        self.btnL.setStyleSheet(btn_style)

        # set Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnL)
        hbox.addStretch(1)
        hbox.addWidget(self.btnR)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.time_edit)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def connectSignal(self):
        self.time_edit.timeChanged.connect(self.changeTime)
        self.btnR.clicked.connect(self.btnClickedEvent)
        self.btnL.clicked.connect(self.btnClickedEvent)

    def changeTime(self, t):
        self.time = t

    def btnClickedEvent(self):
        sender = self.sender()

        if sender is self.btnR:
            # Detamine
            self.valueChanged.emit(self.time)

        elif sender is self.btnL:
            # Cansel
            pass

        self.close()

# for debug
#
# if __name__ == '__main__':
#     from PyQt5.QtWidgets import QApplication
#     import sys
#     def ppprint(t):
#         print(t)

#     app = QApplication(sys.argv)
#     window = InputWindow()
#     window.valueChanged.connect(ppprint)
#     window.show()
#     sys.exit(app.exec_())