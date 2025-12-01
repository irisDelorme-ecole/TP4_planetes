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

        self.asteroid = None


        self.update()


    def update_asteroid(self, asteroid):
        print(asteroid.position)
        self.asteroid = asteroid
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)


        #pour background
        p.setBrush(Qt.GlobalColor.gray)
        p.drawRect(0, 0, 800, 400)

        #planete de base(bouge pas pour maintenant)
        p.setBrush(Qt.GlobalColor.black)
        p.drawEllipse(400, 200,90, 90)

        if self.asteroid is not None:
            p.setBrush(Qt.GlobalColor.blue)
            print("here")
            p.drawEllipse(int(self.asteroid.position[0]), int(self.flip_pymunk_to_qt(8, self.asteroid.position)[1]), 30, 30)


    def flip_pymunk_to_qt(self, height, position):
        return int(position[0]), int(position[1]-height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

