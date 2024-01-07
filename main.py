import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
# ЕСЛИ не работает конвертация интерфейса командой pyuic5 UI.ui -o ui_file.py
# ЗАПУСТИТЬ pip install PyQT5==5.9


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 578)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Make More"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.arr = []

        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def drawCircle(self, qp):
        radius = randint(50, 150)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 55))
        color2 = QColor(randint(0, 255), randint(0, 255), randint(0, 55))
        self.arr.append((randint(-10, self.width()), randint(-10, self.height()), radius, radius, color, color2))
        for i in self.arr:
            pen = QPen(i[-1], 10)  # Pen color
            qp.setPen(pen)
            qp.setBrush(i[-2])  # Fill color
            qp.drawEllipse(*i[:-2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook

    sys.exit(app.exec_())
