from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont, QIcon


class Ui_MainWindow(object):

    def toNext(self, MainWindow):
        from awal import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def toExit(self, MainWindow):
        import sys
        sys.exit(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QIcon("assets/icon.png"))
        MainWindow.setFixedSize(640, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 640, 420))
        self.bg.setPixmap(QPixmap("assets/bg-app.png"))
        self.bg.setScaledContents(True)
        font16 = QFont()
        font16.setPixelSize(20)
        font14 = QFont()
        font14.setPixelSize(18)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(225, 60, 200, 200))
        self.logo.setPixmap(QPixmap("assets/logo.png"))
        self.logo.setScaledContents(True)

        self.label_Umur = QtWidgets.QLabel(self.centralwidget)
        self.label_Umur.setGeometry(QtCore.QRect(170, 20, 400, 40))
        self.label_Umur.setText("Selamat Datang Di Alat Althea")
        self.label_Umur.setFont(font16)

        self.pushButton_Next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Next.setGeometry(QtCore.QRect(350, 320, 181, 61))
        self.pushButton_Next.setText("Mulai")
        self.pushButton_Next.clicked.connect(lambda: self.toNext(MainWindow))
        self.pushButton_Next.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid "
            "white;font-size:20px;background-color:#03dbfc;"
        )

        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(120, 320, 181, 61))
        self.pushButton_Exit.setText("Keluar")
        self.pushButton_Exit.clicked.connect(lambda: self.toExit(MainWindow))
        self.pushButton_Exit.setStyleSheet(
            "border-radius : 28; color:white;font-weight: 600; border: 2 solid "
            "white;font-size:20px;background-color:#F73838;"
        )

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
