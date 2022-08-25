from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    data = {
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
    }

    def toNext(self, MainWindow):
        try:
            if self.radioButton_LakiLaki.isChecked():
                self.data["gender"] = "Laki-Laki"
            elif self.radioButton_Perempuan.isChecked():
                self.data["gender"] = "Perempuan"
            else:
                raise ValueError
        except ValueError:
            print("Gender Unknown")
        else:
            from menu import Ui_MainWindow
            ui = Ui_MainWindow(self.data)
            ui.setupUi(MainWindow)
            MainWindow.show()

    def Up(self):
        self.data["umur"] += 1
        self.label_NilaiUmur.setText(str(self.data["umur"]))

    def Down(self):
        if self.data["umur"] > 0:
            self.data["umur"] -= 1
            self.label_NilaiUmur.setText(str(self.data["umur"]))

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)
        self.label_JenisKelamin = QtWidgets.QLabel(self.centralwidget)
        self.label_JenisKelamin.setGeometry(QtCore.QRect(185, 134, 100, 16))
        self.label_JenisKelamin.setText("Pilih Jenis Kelamin")
        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(220, 24, 91, 16))
        self.label_Umur.setText("Umur")
        self.radioButton_LakiLaki = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_LakiLaki.setGeometry(QtCore.QRect(130, 170, 82, 17))
        self.radioButton_LakiLaki.setText("Laki-laki")
        self.radioButton_Perempuan = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Perempuan.setGeometry(QtCore.QRect(260, 170, 82, 17))
        self.radioButton_Perempuan.setText("Perempuan")

        self.pushButton_UP = PushableLabel(self.centralwidget)
        self.pushButton_UP.setGeometry(QtCore.QRect(250, 94, 60, 23))
        self.pushButton_UP.onMousePressEvent = lambda _: self.Up()
        self.pushButton_UP.setPixmap(QPixmap("assets/arrow-right.png"))
        self.pushButton_UP.setScaledContents(True)

        self.pushButton_DOWN = PushableLabel(self.centralwidget)
        self.pushButton_DOWN.setGeometry(QtCore.QRect(160, 94, 60, 23))
        self.pushButton_DOWN.onMousePressEvent = lambda _: self.Down()
        self.pushButton_DOWN.setPixmap(QPixmap("assets/arrow-left.png"))
        self.pushButton_DOWN.setScaledContents(True)

        self.label_NilaiUmur = QtWidgets.QLabel(self.centralwidget)
        self.label_NilaiUmur.setGeometry(QtCore.QRect(180, 60, 110, 20))
        self.label_NilaiUmur.setText("0")
        self.label_NilaiUmur.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pushButton_Next = PushableLabel(self.centralwidget)
        self.pushButton_Next.setGeometry(QtCore.QRect(240, 230, 181, 61))
        self.pushButton_Next.setPixmap(QPixmap("assets/selanjutnya2.png"))
        self.pushButton_Next.onMousePressEvent = lambda _: self.toNext(MainWindow)
        self.pushButton_Next.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
