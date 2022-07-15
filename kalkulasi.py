import string

from PyQt6 import QtCore, QtWidgets
import json
import random
import time

from paho.mqtt import client as mqtt_client


class Ui_MainWindow(object):
    broker = 'broker.emqx.io'
    port = 1883
    topic = "ALTHEATESTER/"
    token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    username = 'emqx'
    password = 'public'
    client = mqtt_client.Client()

    def __init__(self, data):
        self.client = self.connect_mqtt()
        self.client.loop_start()
        self.data = data

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publish(self):
        data = random.randint(0, 100)
        msgData = {
            'gender': 'Laki-laki',
            'umur': 3,
            'estimasi_tinggi_badan': 80,
            'estimasi_berat_badan': 18,
            'status_gizi': 'baik',
            'lingkar_kepala': 45,
            'lingkar_lengan': 34
        }
        result = self.client.publish(
            self.topic+self.token,
            json.dumps(msgData),
        )

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
        # self.label_UmurValue.setText(f"{self.data['umur']}")
        self.label_GenderValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GenderValue.setGeometry(QtCore.QRect(270, 90, 101, 21))
        # self.label_GenderValue.setText(self.data['gender'])
        self.label_BeratValue = QtWidgets.QLabel(self.centralwidget)
        self.label_BeratValue.setGeometry(QtCore.QRect(270, 120, 101, 21))
        self.label_BeratValue.setText("")
        self.label_TinggiValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TinggiValue.setGeometry(QtCore.QRect(270, 150, 101, 21))
        self.label_TinggiValue.setText("")
        self.label_GiziValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GiziValue.setGeometry(QtCore.QRect(270, 180, 101, 21))
        self.label_GiziValue.setText("")
        self.label_Token= QtWidgets.QLabel(self.centralwidget)
        self.label_Token.setGeometry(QtCore.QRect(70, 220, 101, 21))
        self.label_Token.setText("Token")
        self.label_TokenValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TokenValue.setGeometry(QtCore.QRect(270, 220, 191, 21))
        self.label_TokenValue.setText(self.token)

        self.pushButton_Simpan.clicked.connect(lambda _: self.publish())
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({})
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
