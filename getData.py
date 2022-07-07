from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.lineEdit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_data.setGeometry(QtCore.QRect(210, 100, 241, 51))
        self.lineEdit_data.setText("Pengambilan Data")
        self.label_judul = QtWidgets.QLabel(self.centralwidget)
        self.label_judul.setGeometry(QtCore.QRect(150, 30, 181, 41))
        self.label_judul.setText("Data Terukur :")
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setGeometry(QtCore.QRect(50, 100, 121, 51))
        self.label_data.setText("label_data")
        self.pushButton_kembali = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kembali.setGeometry(QtCore.QRect(210, 240, 111, 41))
        self.pushButton_kembali.setText("Kembali")
        self.pushButton_simpan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_simpan.setGeometry(QtCore.QRect(340, 240, 111, 41))
        self.pushButton_simpan.setText("Simpan")
        self.label_currentData = QtWidgets.QLabel(self.centralwidget)
        self.label_currentData.setGeometry(QtCore.QRect(50, 175, 121, 41))
        self.label_currentData.setText("Data Sekarang")
        self.label_currentValue = QtWidgets.QLabel(self.centralwidget)
        self.label_currentValue.setGeometry(QtCore.QRect(210, 170, 121, 41))
        self.label_currentValue.setText("DataValue")
        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
