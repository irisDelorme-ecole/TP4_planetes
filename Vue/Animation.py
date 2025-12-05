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
        self.setFixedSize(800, 600)

        self.asteroid = None
        self.planete = None


        self.update()


    def update_anim(self, asteroid, planete):
        print(asteroid.position)
        self.asteroid = asteroid
        self.planete = planete
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)


        #pour background
        p.setBrush(Qt.GlobalColor.white)
        p.drawRect(0, 0, 800, 600)

        #planete de base(bouge pas pour maintenant)
        if self.planete is not None:

            p.setBrush(Qt.GlobalColor.black)
            p.drawEllipse(QPoint(int(self.planete.position[0]), int(self.flip_pymunk_to_qt(600,self.planete.position[1]))),int(self.planete.rayon), int(self.planete.rayon))

        if self.asteroid is not None and self.asteroid.position[0] < 1000 and self.asteroid.position[1] < 1000:
            p.setBrush(Qt.GlobalColor.blue)
            print(self.asteroid.position)
            p.drawEllipse(QPoint(int(self.asteroid.position[0] ), int(self.flip_pymunk_to_qt(600, self.asteroid.position[1]))) , int(self.asteroid.rayon), int(self.asteroid.rayon))
            print(int(self.asteroid.position[0] ), int(self.flip_pymunk_to_qt(600, self.asteroid.position[1])))


    def flip_pymunk_to_qt(self, height, position):
        return  int(height-position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

