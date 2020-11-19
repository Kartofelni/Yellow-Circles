import sys

from PyQt5 import QtCore, QtWidgets

from PyQt5.QtGui import QPainter, QColor
from random import randint


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 225, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить кружки"))


class YellowCircles(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Уже не желтые круги')
        self.setFixedSize(500, 500)

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        cd = QPainter()
        cd.begin(self)
        for _ in range(3):
            self.draw_circle(cd)
        cd.end()

    def paint(self):
        self.repaint()

    def draw_circle(self, cd):
        cd.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        diameter = randint(1, 498)
        cd.drawEllipse(randint(1, 500 - diameter),
                       randint(1, 500 - diameter),
                       diameter,
                       diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())
