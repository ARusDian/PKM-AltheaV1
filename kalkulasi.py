from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont, QIcon


# standar lila laki laki tiap umur
STANDARLILALAKI = [
    1, 15.9, 16.2, 16.7, 17.1, 17.5, 17.9, 18.7, 19, 20, 21, 22.3,
    23.2, 24.7, 25.3, 26.4, 27.8, 28.5, 29.7, 30.8, 30.8, 30.8, 30.8, 30.8, 30.8,
    31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 32.6, 32.6, 32.6,
    32.6, 32.6, 32.6, 32.6, 32.6, 32.6, 32.6, 32.2, 32.2, 32.2, 32.2, 32.2, 32.2,
    32.2, 32.2, 32.2, 32.2, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7, 31.7,
    31.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7
]

# standar lila wanita tiap umur
STANDARLILAWANITA = [
    1, 15.6, 16, 16.7, 16.9, 17.3, 17.6, 18.3, 19.5, 20, 21, 22.4,
    23.7, 25.2, 25.2, 25.4, 25.8, 26.4, 25.8, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5,
    27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 27.7, 29.9, 29.9, 29.9,
    29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9,
    29.9, 29.9, 29.9, 29.9, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3, 30.3,
    30.3, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9, 29.9
]


class Ui_MainWindow(object):
    data = {}

    def __init__(self, data):
        self.data = data
        self.rumus_energi()
        self.status_gizi()
        self.info_gizi()

    # Basal Energy Expenditure
    def rumus_energi(self):
        if self.data["gender"] == "Laki-laki":
            self.data['tinggiBadan'] = 97.252 + (2.645 * self.data['panjangUlna'])
            self.data['beratBadan'] = -93.2 + (3.29 * self.data["lingkarLengan"]) + (0.43 * self.data["tinggiBadan"])
            self.data["BEE"] = 66.5 + (13.75 * self.data['beratBadan']) + (5.003 * self.data['tinggiBadan']) - (
                    6.775 * self.data['umur'])
        elif self.data["gender"] == "Perempuan":
            self.data['tinggiBadan'] = 68.777 + (3.536 * self.data['panjangUlna'])
            self.data['beratBadan'] = -64.6 + 2.15 * self.data['lingkarLengan'] + 0.54 * self.data['tinggiBadan']
            self.data["BEE"] = 655.1 + (9.563 * self.data['beratBadan']) + (1.850 * self.data['tinggiBadan']) - (
                    4.676 * self.data['umur'])

        else:
            self.data['beratBadan'] = "0"

    def status_gizi(self):
        if self.data["gender"] == "Laki-laki":
            self.data['statusGizi'] = self.data["lingkarLengan"] / STANDARLILALAKI[self.data["umur"]] * 100

        elif self.data["gender"] == "Perempuan":
            self.data['statusGizi'] = self.data["lingkarLengan"] / STANDARLILAWANITA[self.data["umur"]] * 100

        else:
            self.data['statusGizi'] = 0

    def info_gizi(self):
        if self.data['statusGizi'] <= 70:
            return "Gizi Buruk"
        elif self.data['statusGizi'] <= 84.9:
            return "Gizi Kurang"
        elif self.data['statusGizi'] <= 109.9:
            return "Gizi Baik"
        elif self.data['statusGizi'] <= 120:
            return "Overweight"
        elif self.data['statusGizi'] > 120:
            return "Obesitas"

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
        from landing import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QIcon("assets/icon.ico"))
        MainWindow.setFixedSize(640, 420)
        MainWindow.setWindowTitle("Althea App")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font18 = QFont()
        font22 = QFont()
        font18.setPixelSize(18)
        font22.setPixelSize(22)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 420))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        self.label_Pilih = QtWidgets.QLabel(self.centralwidget)
        self.label_Pilih.setGeometry(QtCore.QRect(220, 10, 170, 35))
        self.label_Pilih.setText("Hasil Perhitungan")
        self.label_Pilih.setFont(font22)

        self.pushButton_Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(430, 320, 181, 61))
        self.pushButton_Simpan.setText("Simpan")
        self.pushButton_Simpan.setFont(font18)
        self.pushButton_Simpan.clicked.connect(lambda: self.publish(MainWindow))
        self.pushButton_Simpan.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600;"
            "border: 2 solid white;font-size:20px;background-color:#03dbfc;"
        )

        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(20, 320, 181, 61))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.setFont(font18)
        self.pushButton_Kembali.clicked.connect(lambda: self.kembali(MainWindow))
        self.pushButton_Kembali.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600;"
            "border: 2 solid white;font-size:20px;background-color:#03dbfc;"
        )

        self.pushButton_Awal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Awal.setGeometry(QtCore.QRect(225, 320, 181, 61))
        self.pushButton_Awal.setText("Menu")
        self.pushButton_Awal.setFont(font18)
        self.pushButton_Awal.clicked.connect(lambda: self.menu(MainWindow))
        self.pushButton_Awal.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600;"
            "border: 2 solid white;font-size:20px;background-color:#03dbfc;"
        )

        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(70, 60, 171, 21))
        self.label_Umur.setText("Umur  : ")
        self.label_Umur.setFont(font18)

        self.label_JenisKelamin = QtWidgets.QLabel(self.centralwidget)
        self.label_JenisKelamin.setGeometry(QtCore.QRect(70, 90, 171, 21))
        self.label_JenisKelamin.setText("Jenis Kelamin  : ")
        self.label_JenisKelamin.setFont(font18)

        self.label_BeratBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratBadan.setGeometry(QtCore.QRect(70, 120, 210, 21))
        self.label_BeratBadan.setText("Estimasi Berat Badan : ")
        self.label_BeratBadan.setFont(font18)

        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(70, 150, 210, 21))
        self.label_TinggiBadan.setText("Estimasi Tinggi Badan : ")
        self.label_TinggiBadan.setFont(font18)

        self.label_statusGizi = QtWidgets.QLabel(self.centralwidget)
        self.label_statusGizi.setGeometry(QtCore.QRect(70, 180, 171, 21))
        self.label_statusGizi.setText("Status Gizi  : ")
        self.label_statusGizi.setFont(font18)

        self.label_TinggiBadan = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiBadan.setGeometry(QtCore.QRect(70, 210, 171, 21))
        self.label_TinggiBadan.setText("Kebutuhan Energi : ")
        self.label_TinggiBadan.setFont(font18)

        self.label_Suhu = QtWidgets.QLabel(self.centralwidget)
        self.label_Suhu.setGeometry(QtCore.QRect(70, 240, 171, 21))
        self.label_Suhu.setText("Suhu Tubuh : ")
        self.label_Suhu.setFont(font18)

        self.label_UmurValue = QtWidgets.QLabel(self.centralwidget)
        self.label_UmurValue.setGeometry(QtCore.QRect(300, 60, 101, 21))
        self.label_UmurValue.setText(f'{self.data["umur"]} Tahun')
        self.label_UmurValue.setFont(font18)

        self.label_GenderValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GenderValue.setGeometry(QtCore.QRect(300, 90, 101, 21))
        self.label_GenderValue.setText(f'{self.data["gender"]}')
        self.label_GenderValue.setFont(font18)

        self.label_BeratValue = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratValue.setGeometry(QtCore.QRect(300, 120, 111, 21))
        self.label_BeratValue.setText(f"{self.data['beratBadan']:.2f} Kg")
        self.label_BeratValue.setFont(font18)

        self.label_TinggiValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiValue.setGeometry(QtCore.QRect(300, 150, 101, 21))
        self.label_TinggiValue.setText(f"{self.data['tinggiBadan']:.2f} Cm")
        self.label_TinggiValue.setFont(font18)

        self.label_GiziValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziValue.setGeometry(QtCore.QRect(300, 180, 101, 21))
        self.label_GiziValue.setText(f"{self.info_gizi()} - [{self.data['statusGizi']}]")
        self.label_GiziValue.setFont(font18)

        self.label_GiziStatue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziStatue.setGeometry(QtCore.QRect(300, 210, 200, 21))
        self.label_GiziStatue.setText(f"{self.data['BEE'] :.2f}, kkal/hari")
        self.label_GiziStatue.setFont(font18)

        self.label_SuhuStatue = QtWidgets.QLabel(self.centralwidget)
        self.label_SuhuStatue.setGeometry(QtCore.QRect(300, 240, 200, 21))
        self.label_SuhuStatue.setText(f"{self.data['suhu']:.2f} C")
        self.label_SuhuStatue.setFont(font18)

        self.label_Token = QtWidgets.QLabel(self.centralwidget)
        self.label_Token.setGeometry(QtCore.QRect(70, 280, 480, 30))
        self.label_Token.setText("Menuju Ke Halaman Selanjutnya untuk menampilkan Token")
        self.label_Token.setFont(font18)

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    pass
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({
        "umur": 21,
        "gender": "Laki-laki",
        "lingkarLengan": 19.45,
        "lingkarKepala": 0,
        "panjangUlna": 24.902,
        "suhu": 35.27,
    })

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
