from Ui_main import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
import sys, time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_8.mousePressEvent = self.start_game
        self.pushButton_6.mousePressEvent = self.send_name
        self.pushButton_3.mousePressEvent = self.flash_page
        self.show()
        self.flash_page(self)

    def start_game(self, event):
        self.stackedWidget.setCurrentIndex(4)
        QApplication.processEvents()
        time.sleep(0.5)
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_3.setText("")

    def send_name(self, event):
        self.stackedWidget.setCurrentIndex(4)
        QApplication.processEvents()
        time.sleep(0.5)
        a = self.lineEdit_3.text()
        print(a)
        if a == "":
            self.stackedWidget.setCurrentIndex(2)
            self.sleep_time(3000)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def flash_page(self, event):
        self.stackedWidget.setCurrentIndex(4)
        QApplication.processEvents()
        time.sleep(0.5)
        c_time = time.strftime("%H", time.localtime())
        print(c_time)
        if c_time == "00":
            print("时间正确，准予放行")
            self.start_game(event)
        else:
            print("时机未到，请君静候")
            self.stackedWidget.setCurrentIndex(3)

    def close_ie(self):
        self.close()

    def sleep_time(self, sleep_time):
        self.send_time = QTimer(self)
        self.send_time.timeout.connect(self.close_ie)
        self.send_time.start(sleep_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindow()
    sys.exit(app.exec_())
