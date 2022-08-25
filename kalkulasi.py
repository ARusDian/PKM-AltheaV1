from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

from components.PushableLabel import PushableLabel


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

    def menu(self, MainWindow):
        from awal import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(210, 10, 81, 20))
        self.label_Pilih.setText("Perhitungan")

        self.label_BeratBadan = PushableLabel(self.centralwidget)
        self.label_BeratBadan.setGeometry(QtCore.QRect(70, 120, 171, 21))
        self.label_BeratBadan.setText("Estimasi Berat Badan : ")

        self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(340, 270, 111, 41))
        self.pushButton_Simpan.onMousePressEvent = lambda _: self.publish(MainWindow)
        self.pushButton_Simpan.setPixmap(QPixmap("assets/kirim.png"))
        self.pushButton_Simpan.setScaledContents(True)

        self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(100, 270, 111, 41))
        self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))
        self.pushButton_Kembali.setScaledContents(True)

        self.pushButton_Awal = PushableLabel(self.centralwidget)
        self.pushButton_Awal.setGeometry(QtCore.QRect(220, 270, 111, 41))
        self.pushButton_Awal.onMousePressEvent = lambda _: self.menu(MainWindow)
        self.pushButton_Awal.setPixmap(QPixmap("assets/menu-utama.png"))
        self.pushButton_Awal.setScaledContents(True)

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

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({
        "umur": 0,
        "gender": "",
        "lingkarLengan": 0,
        "lingkarKepala": 0,
        "lingkarPerut": 0,
        "lingkarPinggul": 0,
        "tinggiBadan": 0,
        "tinggiLutut": 0,
        "setengahDepan": 0,
        "suhu": 0,
    })
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
