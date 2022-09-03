from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont


# from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data

    def pengambilanData(self, MainWindow, mode):
        if mode == "suhu":
            from getSuhu import Ui_MainWindow
            self.ui = Ui_MainWindow(self.data, mode)
            self.ui.setupUi(MainWindow)
            MainWindow.show()
        else:
            from getData import Ui_MainWindow
            self.ui = Ui_MainWindow(self.data, mode)
            self.ui.setupUi(MainWindow)
            MainWindow.show()

    def resetData(self):
        self.data["lingkarLengan"] = 0
        self.data["lingkarKepala"] = 0
        self.data["setengahDepa"] = 0
        self.data["suhu"] = 0

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
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 420))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        font16 = QFont()
        font16.setPixelSize(20)

        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(90, 10, 180, 25))
        self.label_Pilih.setText("Pilih Pengukuran")
        self.label_Pilih.setFont(font16)

        self.label_hasil = QtWidgets.QLabel(self.centralwidget)
        self.label_hasil.setGeometry(QtCore.QRect(360, 10, 180, 25))
        self.label_hasil.setText("Hasil Pengukuran")
        self.label_hasil.setFont(font16)

        # self.pushButton_LingkarLengan = PushableLabel(self.centralwidget)
        self.pushButton_LingkarLengan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarLengan.setGeometry(QtCore.QRect(80, 40, 181, 61))
        self.pushButton_LingkarLengan.setText("Lingkar Lengan")
        self.pushButton_LingkarLengan.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarLengan"))
        self.pushButton_LingkarLengan.setStyleSheet("border-radius : 28; color:white;font-weight: 600; border: 2 "
                                                    "solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_LingkarLengan.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "lingkarLengan")
        # self.pushButton_LingkarLengan.setPixmap(QPixmap("assets/lingkar-lengan.png"))
        # self.pushButton_LingkarLengan.setScaledContents(True)

        self.label_LingkarLengan = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarLengan.setGeometry(QtCore.QRect(360, 50, 371, 25))
        self.label_LingkarLengan.setText(f'Lingkar Lengan: {self.data["lingkarLengan"]:.2f} cm')
        self.label_LingkarLengan.setFont(font16)

        # self.pushButton_Suhu = PushableLabel(self.centralwidget)
        self.pushButton_Suhu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Suhu.setGeometry(QtCore.QRect(80, 250, 181, 61))
        self.pushButton_Suhu.setText("Suhu")
        self.pushButton_Suhu.clicked.connect(lambda: self.pengambilanData(MainWindow, "suhu"))
        self.pushButton_Suhu.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_Suhu.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "suhu")
        # self.pushButton_Suhu.setPixmap(QPixmap("assets/suhu.png"))
        # self.pushButton_Suhu.setScaledContents(True)

        self.label_Suhu = QtWidgets.QLabel(self.centralwidget)
        self.label_Suhu.setGeometry(QtCore.QRect(360, 260, 371, 25))
        self.label_Suhu.setText(f'Suhu Tubuh: {self.data["suhu"]:.2f} °C')
        self.label_Suhu.setFont(font16)

        # self.pushButton_LingkarKepala = PushableLabel(self.centralwidget)
        self.pushButton_LingkarKepala = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarKepala.setGeometry(QtCore.QRect(80, 110, 181, 61))
        self.pushButton_LingkarKepala.setText("Lingkar Kepala")
        self.pushButton_LingkarKepala.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarKepala"))
        self.pushButton_LingkarKepala.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_LingkarKepala.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "lingkarKepala")
        # self.pushButton_LingkarKepala.setPixmap(QPixmap("assets/lingkar-kepala.png"))
        # self.pushButton_LingkarKepala.setScaledContents(True)

        self.label_LingkarKepala = QtWidgets.QLabel(self.centralwidget)
        self.label_LingkarKepala.setGeometry(QtCore.QRect(360, 120, 371, 25))
        self.label_LingkarKepala.setText(f'Lingkar Kepala: {self.data["lingkarKepala"]} cm')
        self.label_LingkarKepala.setFont(font16)

        # self.pushButton_SetengahDepa = PushableLabel(self.centralwidget)
        self.pushButton_SetengahDepa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetengahDepa.setGeometry(QtCore.QRect(80, 180, 181, 61))
        self.pushButton_SetengahDepa.setText("Setengah Depa")
        self.pushButton_SetengahDepa.clicked.connect(lambda: self.pengambilanData(MainWindow, "setengahDepa"))
        self.pushButton_SetengahDepa.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_SetengahDepa.onMousePressEvent = lambda _: self.pengambilanData(MainWindow, "setengahDepa")
        # self.pushButton_SetengahDepa.setPixmap(QPixmap("assets/setengah-depa.png"))
        # self.pushButton_SetengahDepa.setScaledContents(True)

        self.label_SetengahDepa = QtWidgets.QLabel(self.centralwidget)
        self.label_SetengahDepa.setGeometry(QtCore.QRect(360, 190, 371, 25))
        self.label_SetengahDepa.setText(f'Setengah Depa: {self.data["setengahDepa"]} cm')
        self.label_SetengahDepa.setFont(font16)

        # self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(450, 320, 181, 61))
        self.pushButton_Simpan.setText("Kalkulasi")
        self.pushButton_Simpan.clicked.connect(lambda _: self.kalkulasiData(MainWindow))
        self.pushButton_Simpan.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_Simpan.onMousePressEvent = lambda _: self.kalkulasiData(MainWindow)
        # self.pushButton_Simpan.setPixmap(QPixmap("assets/simpan&kirim.png"))
        # self.pushButton_Simpan.setScaledContents(True)

        # self.pushButton_Reset = PushableLabel(self.centralwidget)
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(250, 320, 181, 61))
        self.pushButton_Reset.setText("Reset")
        self.pushButton_Reset.clicked.connect(self.resetData)
        self.pushButton_Reset.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_Reset.clicked.connect(lambda _: self.resetData(MainWindow))
        # self.pushButton_Reset.setPixmap(QPixmap("assets/reset.png"))
        # self.pushButton_Reset.setScaledContents(True)

        # self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(50, 320, 181, 61))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.clicked.connect(lambda _: self.kembali(MainWindow))
        self.pushButton_Kembali.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid white;font-size:20px;background-color:#03dbfc;")
        # self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        # self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))
        # self.pushButton_Kembali.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({
        "umur": 0,
        "gender": "",
        "lingkarKepala": 0,
        "setengahDepa": 0,
        "lingkarLengan": 0,
        "suhu": 0,
    })
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())