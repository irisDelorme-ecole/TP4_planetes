"""
classe qui gère le widget d'animation
"""
import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QApplication


class Animation(QWidget):


    def __init__(self):
        super().__init__()
        #ne pas changer sauf si changé dans modèle
        self.setFixedSize(800, 400)

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
        p.drawEllipse(QPoint(600, 200),90, 90)

        if self.asteroid is not None:
            p.setBrush(Qt.GlobalColor.blue)
            print(self.asteroid.position)
            p.drawEllipse(QPoint(int(self.asteroid.position[0] ), int(self.flip_pymunk_to_qt(200, self.asteroid.position[1]))) , 30, 30)
            print(int(self.asteroid.position[0] ), int(self.flip_pymunk_to_qt(400, self.asteroid.position[1])))


    def flip_pymunk_to_qt(self, height, position):
        return  int(height-position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

