import string

from PyQt6 import QtCore, QtWidgets
import json
import random

from paho.mqtt import client as mqtt_client


class Ui_MainWindow(object):

    def __init__(self, data):
        self.data = data

    def publish(self,MainWindow):
        from qrConnect import Ui_MainWindow
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        MainWindow.show()

    def kembali(self, MainWindow):
        from menu import Ui_MainWindow
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(210, 10, 81, 20))
        self.label_Pilih.setText("Perhitungan")
        self.pushButton_Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(340, 270, 111, 21))
        self.pushButton_Simpan.setText("Kirim")
        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(100, 270, 111, 21))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.clicked.connect(lambda _: self.kembali(MainWindow))
        self.label_BeratBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratBadan.setGeometry(QtCore.QRect(70, 120, 171, 21))
        self.label_BeratBadan.setText("Estimasi Berat Badan : ")
        self.pushButton_Awal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Awal.setGeometry(QtCore.QRect(220, 270, 111, 21))
        self.pushButton_Awal.setText("Menu Utama")
        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(70, 150, 171, 21))
        self.label_TinggiBadan.setText("Estimasi Tinggi Badan : ")
        self.label_statusGizi = QtWidgets.QLabel(self.centralwidget)
        self.label_statusGizi.setGeometry(QtCore.QRect(70, 180, 171, 21))
        self.label_statusGizi.setText("Status Gizi  : ")
        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(70, 60, 171, 21))
        self.label_Umur.setText("Umur  : ")
        self.label_JenisKelamin = QtWidgets.QLabel(self.centralwidget)
        self.label_JenisKelamin.setGeometry(QtCore.QRect(70, 90, 171, 21))
        self.label_JenisKelamin.setText("Jenis Kelamin  : ")
        self.label_UmurValue = QtWidgets.QLabel(self.centralwidget)
        self.label_UmurValue.setGeometry(QtCore.QRect(270, 60, 101, 21))
        self.label_UmurValue.setText("11")
        # self.label_UmurValue.setText(f"{self.data['umur']}")
        self.label_GenderValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GenderValue.setGeometry(QtCore.QRect(270, 90, 101, 21))
        self.label_GenderValue.setText("Laki - Laki")
        # self.label_GenderValue.setText(self.data['gender'])
        self.label_BeratValue = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratValue.setGeometry(QtCore.QRect(270, 120, 101, 21))
        self.label_BeratValue.setText("18")
        self.label_TinggiValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiValue.setGeometry(QtCore.QRect(270, 150, 101, 21))
        self.label_TinggiValue.setText("80")
        self.label_GiziValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziValue.setGeometry(QtCore.QRect(270, 180, 101, 21))
        self.label_GiziValue.setText("baik")
        self.label_Token= QtWidgets.QLabel(self.centralwidget)
        self.label_Token.setGeometry(QtCore.QRect(70, 220, 381, 21))
        self.label_Token.setText("Menuju Ke Halaman Selanjutnya untuk menampilkan Token")

        self.pushButton_Simpan.clicked.connect(lambda _: self.publish(MainWindow))
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({})
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
