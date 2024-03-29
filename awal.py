from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont


# from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data

    def toNext(self, MainWindow):
        try:
            if self.radioButton_LakiLaki.isChecked():
                self.data["gender"] = "Laki-laki"
            elif self.radioButton_Perempuan.isChecked():
                self.data["gender"] = "Perempuan"
            else:
                raise ValueError
        except ValueError:
            self.label_error.setText("Gender Belum Dipilih")
        else:
            from menu import Ui_MainWindow
            ui = Ui_MainWindow(self.data)
            ui.setupUi(MainWindow)
            MainWindow.show()

    def kembali(self, MainWindow):
        from landing import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def Up(self):
        self.data["umur"] += 1
        self.label_NilaiUmur.setText(f'{self.data["umur"]} Tahun')

    def Down(self):
        if self.data["umur"] > 1:
            self.data["umur"] -= 1
            self.label_NilaiUmur.setText(f'{self.data["umur"]} Tahun')

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(640, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 420))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)
        font16 = QFont()
        font16.setPixelSize(20)

        self.label_JenisKelamin = QtWidgets.QLabel(self.centralwidget)
        self.label_JenisKelamin.setGeometry(QtCore.QRect(240, 180, 200, 16))
        self.label_JenisKelamin.setText("Pilih Jenis Kelamin")
        self.label_JenisKelamin.setFont(font16)

        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(290, 20, 91, 16))
        self.label_Umur.setText("Umur")
        self.label_Umur.setFont(font16)

        self.radioButton_LakiLaki = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_LakiLaki.setGeometry(QtCore.QRect(180, 200, 120, 60))
        self.radioButton_LakiLaki.setText("Laki-laki")
        self.radioButton_LakiLaki.setFont(font16)
        self.radioButton_Perempuan = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Perempuan.setGeometry(QtCore.QRect(360, 200, 120, 60))
        self.radioButton_Perempuan.setText("Perempuan")
        self.radioButton_Perempuan.setFont(font16)

        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(230, 270, 200, 30))
        self.label_error.setFont(font16)
        self.label_error.setStyleSheet("color: red")

        self.pushButton_UP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UP.setGeometry(QtCore.QRect(360, 120, 90, 36))
        self.pushButton_UP.setText(">")
        self.pushButton_UP.clicked.connect(self.Up)
        self.pushButton_UP.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid "
            "white;font-size:20px;background-color:#03dbfc;"
        )

        self.pushButton_DOWN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DOWN.setGeometry(QtCore.QRect(180, 120, 90, 36))
        self.pushButton_DOWN.setText("<")
        self.pushButton_DOWN.clicked.connect(self.Down)
        self.pushButton_DOWN.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid "
            "white;font-size:20px;background-color:#03dbfc;"
        )

        self.label_NilaiUmur = QtWidgets.QLabel(self.centralwidget)
        self.label_NilaiUmur.setGeometry(QtCore.QRect(260, 80, 110, 20))
        self.label_NilaiUmur.setText(f'{self.data["umur"]} Tahun')
        self.label_NilaiUmur.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_NilaiUmur.setFont(font16)

        self.pushButton_Next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Next.setGeometry(QtCore.QRect(360, 320, 181, 61))
        self.pushButton_Next.setText("Selanjutnya")
        self.pushButton_Next.clicked.connect(lambda: self.toNext(MainWindow))
        self.pushButton_Next.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid "
            "white;font-size:20px;background-color:#03dbfc;"
        )

        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(100, 320, 181, 61))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.clicked.connect(lambda: self.kembali(MainWindow))
        self.pushButton_Kembali.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600;"
            "border: 2 solid white;font-size:20px;background-color:#03dbfc;"
        )

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({
        "umur": 1,
        "gender": "",
        "lingkarLengan": 0,
        "lingkarKepala": 0,
        "panjangUlna": 0,
        "suhu": 0,
    })
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
