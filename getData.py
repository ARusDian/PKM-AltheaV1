from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

from SensorModules import RotaryEncoder

import pigpio
from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    currentData = ""
    data = {}
    pos = 3.5000

    def __init__(self, data, currentData):
        self.data = data
        self.currentData = currentData
        self.pi = pigpio.pi()
        self.decoder = RotaryEncoder.decoder(self.pi, 6, 13, self.callback)

    def callback(self,way):
        self.pos += way
        # cm = pos + 3,0
        # self.data[self.currentData] = self.pos
        # self.label_currentValue.setText(str(self.pos))
        # print(f"pos={self.pos}")

    def simpan(self):
        self.data[self.currentData] = self.pos
        self.label_currentValue.setText(f"{self.pos}")

    def kembali(self, MainWindow):
        from menu import Ui_MainWindow
        # self.decoder.cancel()
        # self.pi.stop()
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_data.setGeometry(QtCore.QRect(210, 100, 241, 51))
        self.lineEdit_data.setText("0")

        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(150, 30, 181, 41))
        self.label_judul.setText("Data Terukur : " + self.currentData)

        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setGeometry(QtCore.QRect(50, 100, 121, 51))
        self.label_data.setText(self.currentData)

        self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(60, 240, 181, 61))
        self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))
        self.pushButton_Kembali.setScaledContents(True)

        self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(270, 240, 181, 61))
        self.pushButton_Simpan.onMousePressEvent = lambda x: self.simpan()
        self.pushButton_Simpan.setPixmap(QPixmap("assets/simpan.png"))
        self.pushButton_Simpan.setScaledContents(True)

        self.label_currentData = QtWidgets.QLabel(self.centralwidget)
        self.label_currentData.setGeometry(QtCore.QRect(50, 175, 121, 41))
        self.label_currentData.setText("Data Sekarang")
        self.label_currentValue = QtWidgets.QLabel(self.centralwidget)
        self.label_currentValue.setGeometry(QtCore.QRect(210, 170, 121, 41))
        self.label_currentValue.setText("DataValue")
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
