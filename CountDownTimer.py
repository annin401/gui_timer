# -*- coding: utf-8 -*-
from PyQt5.QtCore import(QObject, QTimer, QTime)

class CountDownTimer(QObject):

    def __init__(self):
        super().__init__()
        self._timer_setting_flag = False
        self._remaining_time = QTime(0,0,0,0)
        self.pacemaker = QTimer()

        self.pacemaker.timeout.connect(self._timerUpdate)

    def isRunning(self):
        return self.pacemaker.isActive()

    def isSet(self):
        return self._timer_setting_flag

    def getRemainingTime(self):
        return self._remaining_time

    def setTime(self):
        # TODO 引数でQtime型を受け取り，remaining timeに入れる
        self._remaining_time.setHMS(0,0,9,0)

    def start(self):
        self.pacemaker.start(1000)

    def stop(self):
        self.pacemaker.stop()

    def _timerUpdate(self):
        self.remaining_time = self.remaining_time.addSecs(-1)

# for debug
#
# if __name__ == '__main__':
#     from PyQt5.QtWidgets import QApplication
#     import sys
#     def ppprint():
#         print(timer.getRemainingTime().toString("hh:mm:ss"))
#     app = QApplication(sys.argv)
#     timer = CountDownTimer()
#     timer.setTime()
#     timer.pacemaker.timeout.connect(ppprint)
#     timer.start()
#     sys.exit(app.exec_())