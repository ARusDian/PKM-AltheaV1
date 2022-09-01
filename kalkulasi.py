from typing import Union, Any

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from cv2 import data

from components.PushableLabel import PushableLabel

# standar lila laki laki tiap umur
STANDARLILALAKI = [1, 15.9, 16.2, 16.7, 17.1, 17.5, 17.9, 18.7, 19, 20, 21, 22.3,
                   23.2, 24.7, 25.3, 26.4, 27.8, 28.5, 29.7, 30.8, 30.8, 30.8, 30.8, 30.8, 30.8,
                   31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 32.6, 32.6, 32.6,
                   32.6, 32.6, 32.6, 32.6, 32.6, 32.6, 32.6, 32.2, 32.2, 32.2, 32.2, 32.2, 32.2,
                   32.2, 32.2, 32.2, 32.2, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7,
                   31.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7]

# standar lila wanita tiap umur
STANDARLILAWANITA = [1, 15.6, 16, 16.7, 16.9, 17.3, 17.6, 18.3, 19.5, 20, 21, 22.4,
            23.7, 25.2, 25.2, 25.4, 25.8, 26.4, 25.8, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5,
            27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 29.9, 29.9, 29.9,
            29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9,
            29.9, 29.9, 29.9, 29.9, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3,
            30.3, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9]

class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data
        self.rumus_energi()
        self.status_gizi()
        self.info_gizi()


    #Basal Energy Expenditure
    def rumus_energi(self):
        self.tinggi_badan = (0.73 * 2 * self.data["setengahDepa"]) + 0.43
        self.bee = 0

        if self.data["gender"] == "Laki-laki":
            self.berat_badan = -93.2 + 3.29 * self.data["lingkarLengan"] + 0.43 * self.tinggi_badan
            self.bee = 66.5 + (13.75 * self.berat_badan) + (5.003 * self.tinggi_badan) - (6.775 * self.data["umur"])

        elif self.data["gender"] == "Perempuan":
            self.berat_badan = -64.6 + 2.15 * self.data["lingkarLengan"] + 0.54 * self.tinggi_badan
            self.bee = 655.1 + (9.563 * self.berat_badan) + (1.850 * self.tinggi_badan) - (4.676 * self.data["umur"])

        else:
            self.berat_badan = "0"

    def status_gizi(self):
        self.statusGizi = 0

        if self.data["gender"] == "Laki-laki":
            self.statusGizi = self.data["lingkarLengan"] / STANDARLILALAKI[self.data["umur"]] * 100

        elif self.data["gender"] == "Perempuan":
            self.statusGizi = self.data["lingkarLengan"] / STANDARLILAWANITA[self.data["umur"]] * 100

        else:
            self.statusGizi = 0

    def info_gizi(self):
        if self.statusGizi <= 70:
            self.infoGizi = "Gizi Buruk"
        elif self.statusGizi <= 84.9:
            self.infoGizi = "Gizi Kurang"
        elif self.statusGizi <= 109.9:
            self.infoGizi = "Gizi Baik"
        elif self.statusGizi <= 120:
            self.infoGizi = "Overweight"
        elif self.statusGizi > 120:
            self.infoGizi = "Obesitas"


    def publish(self, MainWindow):
        from qrConnect import Ui_MainWindow
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        MainWindow.show()

    def kembali(self, MainWindow):
        from menu import Ui_MainWindow
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        MainWindow.show()

    def menu(self, MainWindow):
        from awal import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font16 = QFont()
        font20 = QFont()
        font16.setPixelSize(18)
        font20.setPixelSize(22)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(270, 10, 125, 35))
        self.label_Pilih.setText("Perhitungan")
        self.label_Pilih.setFont(font20)

        self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(430, 380, 181, 61))
        self.pushButton_Simpan.onMousePressEvent = lambda _: self.publish(MainWindow)
        self.pushButton_Simpan.setPixmap(QPixmap("assets/kirim.png"))
        self.pushButton_Simpan.setScaledContents(True)

        self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(20, 380, 181, 61))
        self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))

        self.pushButton_Awal = PushableLabel(self.centralwidget)
        self.pushButton_Awal.setGeometry(QtCore.QRect(225, 380, 181, 61))
        self.pushButton_Awal.onMousePressEvent = lambda _: self.menu(MainWindow)
        self.pushButton_Awal.setPixmap(QPixmap("assets/menu-utama.png"))
        self.pushButton_Awal.setScaledContents(True)

        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(70, 60, 171, 21))
        self.label_Umur.setText("Umur  : ")
        self.pushButton_Kembali.setScaledContents(True)
        self.label_Umur.setFont(font16)

        self.label_JenisKelamin = QtWidgets.QLabel(self.centralwidget)
        self.label_JenisKelamin.setGeometry(QtCore.QRect(70, 90, 171, 21))
        self.label_JenisKelamin.setText("Jenis Kelamin  : ")
        self.label_JenisKelamin.setFont(font16)

        self.label_BeratBadan = PushableLabel(self.centralwidget)
        self.label_BeratBadan.setGeometry(QtCore.QRect(70, 120, 210, 21))
        self.label_BeratBadan.setText("Estimasi Berat Badan : ")
        self.label_BeratBadan.setFont(font16)

        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(70, 150, 171, 21))
        self.label_TinggiBadan.setText("Estimasi Tinggi Badan : ")
        self.label_TinggiBadan.setFont(font16)

        self.label_statusGizi = QtWidgets.QLabel(self.centralwidget)
        self.label_statusGizi.setGeometry(QtCore.QRect(70, 180, 171, 21))
        self.label_statusGizi.setText("Status Gizi  : ")
        self.label_statusGizi.setFont(font16)

        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(70, 210, 171, 21))
        self.label_TinggiBadan.setText("Kebutuhan Energi : ")
        self.label_TinggiBadan.setFont(font16)

        self.label_UmurValue = QtWidgets.QLabel(self.centralwidget)
        self.label_UmurValue.setGeometry(QtCore.QRect(270, 60, 101, 21))
        self.label_UmurValue.setText(f'{self.data["umur"]} Tahun')
        self.label_UmurValue.setFont(font16)

        # self.label_UmurValue.setText(f"{self.data['umur']}")
        self.label_GenderValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GenderValue.setGeometry(QtCore.QRect(270, 90, 101, 21))
        self.label_GenderValue.setText(f'{self.data["gender"]}')
        self.label_GenderValue.setFont(font16)

        # self.label_GenderValue.setText(self.data['gender'])

        self.label_BeratValue = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratValue.setGeometry(QtCore.QRect(270, 120, 111, 21))
        self.label_BeratValue.setText(f'{self.berat_badan} Kg')
        self.label_BeratValue.setFont(font16)

        self.label_TinggiValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiValue.setGeometry(QtCore.QRect(270, 150, 101, 21))
        self.label_TinggiValue.setText(f'{self.tinggi_badan} Cm')
        self.label_TinggiValue.setFont(font16)

        self.label_GiziValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziValue.setGeometry(QtCore.QRect(270, 180, 101, 21))
        self.label_GiziValue.setText(f"{self.infoGizi}")
        self.label_GiziValue.setFont(font16)

        self.label_GiziStatue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziStatue.setGeometry(QtCore.QRect(270, 210, 200, 21))
        self.label_GiziStatue.setText(f"{self.bee}, kkal/hari")
        self.label_GiziStatue.setFont(font16)

        self.label_Token= QtWidgets.QLabel(self.centralwidget)
        self.label_Token.setGeometry(QtCore.QRect(70, 340, 480, 21))
        self.label_Token.setText("Menuju Ke Halaman Selanjutnya untuk menampilkan Token")
        self.label_Token.setFont(font16)

        MainWindow.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    pass
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({
        "umur": 0,
        "gender": "Laki-laki",
        "lingkarLengan": 0,
        "lingkarKepala": 0,
        "setengahDepa": 0,
        "suhu": 0,
    })

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
