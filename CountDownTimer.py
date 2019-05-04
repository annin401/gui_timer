# -*- coding: utf-8 -*-
from enum import Enum, auto
from PyQt5.QtCore import(QObject, QTimer, QTime, pyqtSignal, pyqtBoundSignal)

class CountDownTimer(QObject):

    timerFinished = pyqtSignal() # don't put pyqtSignal in __init__(self)

    def __init__(self):
        super().__init__()
        self.pacemaker = QTimer()
        self._timer_status = TimerStatus.SETTING
        self._remaining_time = QTime(0,0,0,0)
        self.__time_zero = QTime(0,0,0,0)

        self.pacemaker.timeout.connect(self._timerUpdate)

    def getTimerStatus(self):
        return self._timer_status

    def getRemainingTime(self):
        return self._remaining_time

    def setTime(self):
        # TODO 引数でQtime型を受け取り，remaining timeに入れる
        self._remaining_time.setHMS(0,0,9,0)

    def start(self):
        self.pacemaker.start(1000)
        self._timer_status = TimerStatus.RUNNING

    def stop(self):
        self.pacemaker.stop()
        self._timer_status = TimerStatus.PAUSING

    def _timerUpdate(self):
        if self._remaining_time == self.__time_zero:
            self.pacemaker.stop()
            self._timer_status = TimerStatus.FINISHED
            self.timerFinished.emit()
            return

        self._remaining_time = self._remaining_time.addSecs(-1)

class TimerStatus(Enum):
    SETTING = auto()
    RUNNING = auto()
    PAUSING = auto()
    FINISHED = auto()

# for debug
#
# if __name__ == '__main__':
#     from PyQt5.QtWidgets import QApplication
#     import sys
#     def ppprint():
#         print(timer.getRemainingTime().toString("hh:mm:ss"))
#         print(timer.getTimerStatus())
#     def printF():
#         print("Finish")
#     app = QApplication(sys.argv)
#     timer = CountDownTimer()
#     timer.setTime()
#     timer.pacemaker.timeout.connect(ppprint)
#     timer.start()
#     timer.timerFinished.connect(printF)
#     sys.exit(app.exec_())