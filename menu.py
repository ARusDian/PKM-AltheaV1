from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data

    def pengambilanData(self, MainWindow, mode):
        if mode == "suhu":
            from getSuhu import Ui_MainWindow
            self.ui = Ui_MainWindow(self.data,mode)
            self.ui.setupUi(MainWindow)
            MainWindow.show()
        else:
            from getData import Ui_MainWindow
            self.ui = Ui_MainWindow(self.data, mode)
            self.ui.setupUi(MainWindow)
            MainWindow.show()

    def kalkulasiData(self, MainWindow):
        from kalkulasi import Ui_MainWindow
        self.ui = Ui_MainWindow(self.data)
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def kembali(self, MainWindow):
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
        self.label_Pilih.setGeometry(QtCore.QRect(60, 10, 120, 25))
        self.label_Pilih.setText("Pilih Pengukuran")

        self.pushButton_LingkarLengan = PushableLabel(self.centralwidget)
        self.pushButton_LingkarLengan.setGeometry(QtCore.QRect(10, 40, 141, 35))
        self.pushButton_LingkarLengan.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "lingkarLengan")
        self.pushButton_LingkarLengan.setPixmap(QPixmap("assets/lingkar-lengan.png"))
        self.pushButton_LingkarLengan.setScaledContents(True)

        self.pushButton_LingkarKepala = PushableLabel(self.centralwidget)
        self.pushButton_LingkarKepala.setGeometry(QtCore.QRect(10, 70, 141, 35))
        self.pushButton_LingkarKepala.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "lingkarKepala")
        self.pushButton_LingkarKepala.setPixmap(QPixmap("assets/lingkar-kepala.png"))
        self.pushButton_LingkarKepala.setScaledContents(True)

        self.pushButton_LingkarPerut = PushableLabel(self.centralwidget)
        self.pushButton_LingkarPerut.setGeometry(QtCore.QRect(10, 100, 141, 35))
        self.pushButton_LingkarPerut.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "lingkarPerut")
        self.pushButton_LingkarPerut.setPixmap(QPixmap("assets/lingkar-perut.png"))
        self.pushButton_LingkarPerut.setScaledContents(True)

        self.pushButton_LingkarPinggul = PushableLabel(self.centralwidget)
        self.pushButton_LingkarPinggul.setGeometry(QtCore.QRect(10, 130, 141, 35))
        self.pushButton_LingkarPinggul.onMousePressEvent = lambda: self.pengambilanData(MainWindow, "lingkarPinggul")
        self.pushButton_LingkarPinggul.setPixmap(QPixmap("assets/lingkar-pinggul.png"))
        self.pushButton_LingkarPinggul.setScaledContents(True)

        self.pushButton_TinggiBadan = PushableLabel(self.centralwidget)
        self.pushButton_TinggiBadan.setGeometry(QtCore.QRect(10, 160, 141, 35))
        self.pushButton_TinggiBadan.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "tinggiBadan")
        self.pushButton_TinggiBadan.setPixmap(QPixmap("assets/tinggi-badan.png"))
        self.pushButton_TinggiBadan.setScaledContents(True)

        self.pushButton_TinggiLutut = PushableLabel(self.centralwidget)
        self.pushButton_TinggiLutut.setGeometry(QtCore.QRect(10, 190, 141, 35))
        self.pushButton_TinggiLutut.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "tinggiLutut")
        self.pushButton_TinggiLutut.setPixmap(QPixmap("assets/tinggi-lutut.png"))
        self.pushButton_TinggiLutut.setScaledContents(True)

        self.pushButton_SetengahDepan = PushableLabel(self.centralwidget)
        self.pushButton_SetengahDepan.setGeometry(QtCore.QRect(10, 220, 141, 35))
        self.pushButton_SetengahDepan.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "setengahDepan")
        self.pushButton_SetengahDepan.setPixmap(QPixmap("assets/setengah-depa.png"))
        self.pushButton_SetengahDepan.setScaledContents(True)

        self.pushButton_Suhu = PushableLabel(self.centralwidget)
        self.pushButton_Suhu.setGeometry(QtCore.QRect(10, 250, 141, 35))
        self.pushButton_Suhu.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "suhu")
        self.pushButton_Suhu.setPixmap(QPixmap("assets/suhu.png"))
        self.pushButton_Suhu.setScaledContents(True)

        self.label_LingkarLengan = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarLengan.setGeometry(QtCore.QRect(210, 40, 371, 25))
        self.label_LingkarLengan.setText(f'Lingkar Lengan: {self.data["lingkarLengan"]} cm')
        self.label_hasil = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil.setGeometry(QtCore.QRect(260, 10, 111, 25))
        self.label_hasil.setText("Hasil Pengukuran")
        self.label_LingkarKepala = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarKepala.setGeometry(QtCore.QRect(210, 70, 371, 25))
        self.label_LingkarKepala.setText(f'Lingkar Kepala: {self.data["lingkarKepala"]} cm')
        self.label_LingkarPerut = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarPerut.setGeometry(QtCore.QRect(210, 100, 371, 25))
        self.label_LingkarPerut.setText(f'Lingkar Perut: {self.data["lingkarPerut"]} cm')
        self.label_LingkarPinggul = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarPinggul.setGeometry(QtCore.QRect(210, 130, 371, 25))
        self.label_LingkarPinggul.setText(f'Lingkar Pinggul: {self.data["lingkarPinggul"]} cm')
        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(210, 160, 371, 25))
        self.label_TinggiBadan.setText(f'Tinggi Badan: {self.data["tinggiBadan"]} cm')
        self.label_TinggiLutut = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiLutut.setGeometry(QtCore.QRect(210, 190, 371, 25))
        self.label_TinggiLutut.setText(f'Tinggi Lutut: {self.data["tinggiLutut"]} cm')
        self.label_SetengahDepan = QtWidgets.QLabel(self.centralwidget)
        self.label_SetengahDepan.setGeometry(QtCore.QRect(210, 220, 371, 25))
        self.label_SetengahDepan.setText(f'Setengah Depan: {self.data["setengahDepan"]} cm')
        self.label_Suhu = QtWidgets.QLabel(self.centralwidget)
        self.label_Suhu.setGeometry(QtCore.QRect(210, 250, 371, 25))
        self.label_Suhu.setText(f'Suhu Tubuh: {self.data["suhu"]} °C')

        self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(330, 285, 111, 35))
        self.pushButton_Simpan.setText("Simpan dan Kirim")
        self.pushButton_Simpan.onMousePressEvent = lambda _: self.kalkulasiData(MainWindow)
        self.pushButton_Simpan.setPixmap(QPixmap("assets/simpan&kirim.png"))
        self.pushButton_Simpan.setScaledContents(True)

        self.pushButton_Reset = PushableLabel(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(210, 285, 111, 35))
        self.pushButton_Reset.setText("Reset")
        self.pushButton_Reset.setPixmap(QPixmap("assets/reset.png"))
        self.pushButton_Reset.setScaledContents(True)

        self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(90, 285, 111, 35))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))
        self.pushButton_Kembali.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({})
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
