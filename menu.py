from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data

    def pengambilanData(self, MainWindow, mode):
        from getData import Ui_MainWindow
        self.ui = Ui_MainWindow(self.data, mode)
        self.ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(60, 10, 120, 25))
        self.label_Pilih.setText("Pilih Pengukuran")

        self.pushButton_LingkarLengan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarLengan.setGeometry(QtCore.QRect(10, 40, 181, 25))
        self.pushButton_LingkarLengan.setText("Lingkar Lengan")
        self.pushButton_LingkarLengan.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarLengan"))

        self.pushButton_LingkarKepala = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarKepala.setGeometry(QtCore.QRect(10, 70, 181, 25))
        self.pushButton_LingkarKepala.setText("Lingkar Kepala")
        self.pushButton_LingkarKepala.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarKepala"))

        self.pushButton_LingkarPerut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarPerut.setGeometry(QtCore.QRect(10, 100, 181, 25))
        self.pushButton_LingkarPerut.setText("Lingkar Perut")
        self.pushButton_LingkarPerut.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarPerut"))

        self.pushButton_LingkarPinggul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LingkarPinggul.setGeometry(QtCore.QRect(10, 130, 181, 25))
        self.pushButton_LingkarPinggul.setText("Lingkar Pinggul")
        self.pushButton_LingkarPinggul.clicked.connect(lambda: self.pengambilanData(MainWindow, "lingkarPinggul"))

        self.pushButton_TinggiBadan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TinggiBadan.setGeometry(QtCore.QRect(10, 160, 181, 25))
        self.pushButton_TinggiBadan.setText("Tinggi Badan")
        self.pushButton_TinggiBadan.clicked.connect(lambda: self.pengambilanData(MainWindow, "tinggiBadan"))

        self.pushButton_TinggiLutut = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_TinggiLutut.setGeometry(QtCore.QRect(10, 190, 181, 25))
        self.pushButton_TinggiLutut.setText("Tinggi Lutut")
        self.pushButton_TinggiLutut.clicked.connect(lambda: self.pengambilanData(MainWindow, "tinggiLutut"))

        self.pushButton_SetengahDepan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetengahDepan.setGeometry(QtCore.QRect(10, 220, 181, 25))
        self.pushButton_SetengahDepan.setText("Setengah Depan")
        self.pushButton_SetengahDepan.clicked.connect(lambda: self.pengambilanData(MainWindow, "setengahDepan"))

        self.pushButton_Suhu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Suhu.setGeometry(QtCore.QRect(10, 250, 181, 25))
        self.pushButton_Suhu.setText("Suhu")
        self.pushButton_Suhu.clicked.connect(lambda: self.pengambilanData(MainWindow, "suhu"))

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
        self.pushButton_Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(330, 285, 111, 25))
        self.pushButton_Simpan.setText("Simpan dan Kirim")
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(210, 285, 111, 25))
        self.pushButton_Reset.setText("Reset")
        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(90, 285, 111, 25))
        self.pushButton_Kembali.setText("Kembali")
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({})
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
