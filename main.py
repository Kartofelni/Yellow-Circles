import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Желтые круги')
        self.setFixedSize(500, 500)

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        cd = QPainter()
        cd.begin(self)
        cd.setBrush(QColor(240, 200, 0))
        for _ in range(3):
            self.draw_circle(cd)
        cd.end()

    def paint(self):
        self.repaint()

    def draw_circle(self, cd):
        diameter = randint(1, 498)
        cd.drawEllipse(randint(1, 500 - diameter),
                       randint(1, 500 - diameter),
                       diameter,
                       diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())
