import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
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
        color = QColor(randint(200, 255), randint(200, 255), randint(0, 55))
        color2 = QColor(randint(200, 255), randint(200, 255), randint(0, 55))
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
