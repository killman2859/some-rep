import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.paint = False

    def paintEvent(self, event):
        if self.paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = randint(100, 500)
            qp.drawEllipse(100, 100, r, r)
            # Завершаем рисование
            qp.end()

    def run(self):
        self.paint = True
        self.update()  # Обновляем виджет для отображения рисунка


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
