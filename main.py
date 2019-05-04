# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QIcon, QFont)
from CountDownTimer import (CountDownTimer, TimerStatus)

class MainWindow(QWidget):

   def __init__(self):
        super().__init__()

        self.cdTimer = CountDownTimer()

        self.createUI()
        self.connectSignal()

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
        self.btnL = QPushButton("Set", self)
        self.btnR.setFixedSize(70, 30)
        self.btnL.setFixedSize(70, 30)

        # Create Label for display
        self.__remaining_time = self.cdTimer.getRemainingTime().toString("hh:mm:ss")
        self.lbl = QLabel(self.__remaining_time, self) 
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

   def connectSignal(self):
        self.btnR.clicked.connect(self.btnClickedEvent)
        self.btnL.clicked.connect(self.btnClickedEvent)
        self.cdTimer.pacemaker.timeout.connect(self.updateLabel)
        self.cdTimer.timerFinished.connect(self.musicPlay)

   def btnClickedEvent(self):
        sender = self.sender()
        timerStatus = self.cdTimer.getTimerStatus()

        if sender is  self.btnR:

            if timerStatus == TimerStatus.SETTING:
                # Start
                self.cdTimer.start()
                self.toggle_To_RUNNING_Button()

            elif timerStatus == TimerStatus.RUNNING:
                # Pause
                self.cdTimer.stop()
                self.toggle_To_PAUSING_Button()

            elif timerStatus == TimerStatus.PAUSING:
                # Restart
                self.cdTimer.start()
                self.toggle_To_RUNNING_Button()

            elif timerStatus == TimerStatus.FINISHED:
                # Stop
                self.cdTimer.reset()
                self.toggle_To_SETTING_Button()
                
        elif sender is self.btnL:    

            if timerStatus == TimerStatus.SETTING:
                # Set
                pass # TODO
                self.cdTimer.setTime() # かり
                self.updateLabel()

            elif timerStatus == TimerStatus.PAUSING:    
                # Reset
                self.cdTimer.reset()
                self.toggle_To_SETTING_Button()
                self.updateLabel()

   def toggle_To_SETTING_Button(self):
                self.btnR.setText("Start")
                self.btnL.setText("Set")

   def toggle_To_RUNNING_Button(self):
                self.btnR.setText("Pause")
                self.btnL.setText("")

   def toggle_To_PAUSING_Button(self):
                self.btnR.setText("Restart")
                self.btnL.setText("Reset")

   def toggle_To_FINISHED_Button(self):
                self.btnR.setText("Stop")
                self.btnL.setText("")

   def updateLabel(self):
       self.__remaining_time = self.cdTimer.getRemainingTime().toString("hh:mm:ss")
       self.lbl.setText(self.__remaining_time)


   def musicPlay(self):
        pass # TODO


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())