from PyQt5 import QtWidgets


class PushableLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super(QtWidgets.QLabel, self).__init__(parent)
        super().__init__(parent)
        self.onMousePressEvent = lambda _: None

    def mousePressEvent(self, event):
        self.onMousePressEvent(event)
