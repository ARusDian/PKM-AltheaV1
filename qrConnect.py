import json
import string

from PyQt5 import QtCore, QtWidgets, QtGui
from PIL.ImageQt import ImageQt
import random
import qrcode
from PyQt5.QtGui import QPixmap

from paho.mqtt import client as mqtt_client

# from components.PushableLabel import PushableLabel


class Ui_MainWindow(object):
    data = {}
    broker = 'broker.emqx.io'
    port = 1883
    topic = "ALTHEATESTER/"
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    username = 'emqx'
    password = 'public'
    client = mqtt_client.Client()

    def publish(self):
        result = self.client.publish(
            self.topic + self.token,
            json.dumps(self.data),
        )

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

    def menu(self, MainWindow):
        self.client.loop_stop()
        from awal import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def kembali(self, MainWindow):
        # self._mutex.lock()
        self.client.loop_stop()
        from kalkulasi import Ui_MainWindow
        ui = Ui_MainWindow(self.data)
        ui.setupUi(MainWindow)
        # self._mutex.unlock()
        MainWindow.show()

    def __init__(self, data):
        self.token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
        self.client = self.connect_mqtt()
        self.client.loop_start()
        # self.msgData = {
        #     'gender': 'Laki-laki',
        #     'umur': 3,
        #     'estimasi_tinggi_badan': 80,
        #     'estimasi_berat_badan': 18,
        #     'status_gizi': 'baik',
        #     'lingkar_kepala': 45,
        #     'lingkar_lengan': 34
        # }
        self.data = data

    def setupUi(self, MainWindow):
        MainWindow.resize(640, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 420))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)

        self.label_QrToken = QtWidgets.QLabel(self.centralwidget)
        self.label_QrToken.setGeometry(QtCore.QRect(10, -20, 300, 300))
        self.label_QrToken.setPixmap(QtGui.QPixmap.fromImage(ImageQt((qrcode.make(self.token)))))
        self.label_Token = QtWidgets.QLabel(self.centralwidget)
        self.label_Token.setGeometry(QtCore.QRect(325, 150, 101, 21))
        self.label_Token.setText("Token")
        font_tokenlabel = QtGui.QFont()
        font_tokenlabel.setPointSize(12)
        font_tokenlabel.setBold(True)
        self.label_Token.setFont(font_tokenlabel)
        self.label_TokenValue = QtWidgets.QLabel(self.centralwidget)
        self.label_TokenValue.setGeometry(QtCore.QRect(300, 170, 150, 50))
        self.label_TokenValue.setText(self.token)
        font_token = QtGui.QFont()
        font_token.setPointSize(18)
        font_token.setBold(True)
        font_btn = QtGui.QFont()
        font_btn.setPointSize(14)
        self.label_TokenValue.setFont(font_token)
        # self.pushButton_Simpan = PushableLabel(self.centralwidget)
        self.pushButton_Simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Simpan.setGeometry(QtCore.QRect(340, 270, 111, 41))
        self.pushButton_Simpan.setText("Kirim Data")
        self.pushButton_Simpan.setFont(font_btn)
        self.pushButton_Simpan.clicked.connect(lambda: self.publish())
        # self.pushButton_Simpan.onMousePressEvent = lambda _: self.publish()
        # self.pushButton_Simpan.setPixmap(QPixmap("assets/kirim.png"))
        # self.pushButton_Simpan.setScaledContents(True)

        # self.pushButton_Kembali = PushableLabel(self.centralwidget)
        self.pushButton_Kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kembali.setGeometry(QtCore.QRect(100, 270, 111, 41))
        self.pushButton_Kembali.setText("Kembali")
        self.pushButton_Kembali.setFont(font_btn)
        self.pushButton_Kembali.clicked.connect(lambda: self.kembali(MainWindow))
        # self.pushButton_Kembali.onMousePressEvent = lambda _: self.kembali(MainWindow)
        # self.pushButton_Kembali.setPixmap(QPixmap("assets/kembali.png"))
        # self.pushButton_Kembali.setScaledContents(True)

        # self.pushButton_Awal = PushableLabel(self.centralwidget)
        self.pushButton_Awal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Awal.setGeometry(QtCore.QRect(220, 270, 111, 41))
        self.pushButton_Awal.setText("Menu Utama")
        self.pushButton_Awal.setFont(font_btn)
        self.pushButton_Awal.clicked.connect(lambda: self.menu(MainWindow))
        # self.pushButton_Awal.onMousePressEvent = lambda _: self.menu(MainWindow)
        # self.pushButton_Awal.setPixmap(QPixmap("assets/menu-utama.png"))
        # self.pushButton_Awal.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)





if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow({})
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
