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
        self.setFixedSize(800, 400)
        self.update()


    def paintEvent(self, event):
        p = QPainter(self)


        #pour background
        p.setBrush(Qt.GlobalColor.gray)
        p.drawRect(0, 0, 800, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

