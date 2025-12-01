"""
classe qui gère le widget d'animation
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QApplication


class Animation(QWidget):


    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.update()


    def paintEvent(self, event):
        p = QPainter(self)


        #pour background
        p.setBrush(Qt.GlobalColor.gray)
        p.drawRect(0, 0, 600, 400)

        #planete de base(bouge pas pour maintenant)
        p.setBrush(Qt.GlobalColor.black)
        p.drawEllipse(400, 200,30, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

