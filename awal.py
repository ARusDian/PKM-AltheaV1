from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt


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
        self.pushButton_UP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UP.setGeometry(QtCore.QRect(240, 94, 75, 23))
        self.pushButton_UP.setText(">")
        self.pushButton_UP.clicked.connect(self.Up)
        self.pushButton_DOWN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DOWN.setGeometry(QtCore.QRect(160, 94, 75, 23))
        self.pushButton_DOWN.setText("<")
        self.pushButton_DOWN.clicked.connect(self.Down)
        self.label_NilaiUmur = QtWidgets.QLabel(self.centralwidget)
        self.label_NilaiUmur.setGeometry(QtCore.QRect(180, 60, 110, 20))
        self.label_NilaiUmur.setText("0")
        self.label_NilaiUmur.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_Next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Next.setGeometry(QtCore.QRect(320, 230, 111, 21))
        self.pushButton_Next.setText("Selanjutnya")
        self.pushButton_Next.clicked.connect(lambda x: self.toNext(MainWindow))
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
