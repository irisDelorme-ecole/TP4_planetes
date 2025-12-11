"""
classe qui gère le widget d'animation
"""
import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget, QApplication


class Animation(QWidget):

    SCALE = 500/(0.5e8)

    def __init__(self):
        super().__init__()
        #ne pas changer sauf si changé dans modèle
        self.setFixedSize(1000, 800)

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
        p.setBrush(Qt.GlobalColor.black)
        p.drawRect(0, 0, 1000, 800)

        #planete de base(bouge pas pour maintenant)
        if self.planete is not None:

            p.setBrush(Qt.GlobalColor.yellow)
            p.drawEllipse(self.scaled_point(self.planete.position),int(self.planete.nb_terres*4), int(self.planete.nb_terres*4))

        if self.asteroid is not None:
            p.setBrush(Qt.GlobalColor.blue)
            print(self.asteroid.position)
            p.drawEllipse(self.scaled_point(self.asteroid.position) , int(self.asteroid.nb_terres*5), int(self.asteroid.nb_terres*5))
            print(int(self.asteroid.rayon/100))
            print(int(self.asteroid.position[0] ), int(self.flip_pymunk_to_qt(800, self.asteroid.position[1])))

        p.setPen(Qt.GlobalColor.white)
        p.drawText(QPoint(850, 750), "Soleil PAS à l'échelle")


    def scaled_point(self, position):
        print(QPoint(int(self.SCALE*position[0]), self.flip_pymunk_to_qt(800,self.SCALE*position[1])), "POS SCALED")
        return QPoint(int(self.SCALE*position[0]), self.flip_pymunk_to_qt(800,self.SCALE*position[1]))

    def flip_pymunk_to_qt(self, height, position):
        return  int(height-position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Animation()
    window.show()
    sys.exit(app.exec())

