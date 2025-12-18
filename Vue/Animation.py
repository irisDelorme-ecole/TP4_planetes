"""
classe qui gère le widget d'animation
"""
import sys

from PyQt6.QtCore import Qt, QPoint, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class Animation(QWidget):

    request_drag = pyqtSignal(str, float, float)
    request_release = pyqtSignal()

    SCALE = 500/(0.5e8)

    def __init__(self):
        super().__init__()
        #ne pas changer sauf si changé dans modèle
        self.setFixedSize(1000, 700)
        self.autoriser_interaction = True
        self.asteroid = None
        self.planete = None

        self.dragging = False
        self.target = None

        self.update()

        self.drag_offset_x = 0
        self.drag_offset_y = 100


    def update_anim(self, asteroid, planete):
        #print(asteroid.position)
        self.asteroid = asteroid
        self.planete = planete
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)


        #pour background
        p.setBrush(Qt.GlobalColor.black)
        p.drawRect(0, 0, 1000, 700)

        #planete de base(bouge pas pour maintenant)
        if self.planete is not None:
            p.setBrush(Qt.GlobalColor.yellow)
            p.drawEllipse(self.scaled_point(self.planete.position), int(self.planete.nb_terres * 4),
                          int(self.planete.nb_terres * 4))

        if self.asteroid is not None:
            print(self.asteroid.couleur)
            p.setBrush(QColor(self.asteroid.couleur))
            #p.setBrush(Qt.GlobalColor.blue)
            #print(self.asteroid.position)
            p.drawEllipse(self.scaled_point(self.asteroid.position), int(self.asteroid.nb_terres * 5),
                          int(self.asteroid.nb_terres * 5))
            #print(int(self.asteroid.rayon / 100))
            #print(int(self.asteroid.position[0]), int(self.flip_pymunk_to_qt(800, self.asteroid.position[1])))

        p.setPen(Qt.GlobalColor.white)
        p.drawText(QPoint(850, 680), "Soleil PAS à l'échelle")


    def scaled_point(self, position):
        #print(QPoint(int(self.SCALE*position[0]), self.flip_pymunk_to_qt(600,self.SCALE*position[1])), "POS SCALED")
        return QPoint(int(self.SCALE*position[0]), self.flip_pymunk_to_qt(700,self.SCALE*position[1]))

    def flip_pymunk_to_qt(self, height, position):
        return  int(height-position)

    def mousePressEvent(self, event):
     if self.autoriser_interaction:
        if event.button() != Qt.MouseButton.LeftButton:
            return
        pos = event.pos()

        #if self.planete and self._hit(self.planete, pos):
            #self.dragging = True
            #self.target = "planete"
            #self.request_drag.emit(self.target, pos.x() + self.drag_offset_x, pos.y() + self.drag_offset_y)

        if self.asteroid and self._hit(self.asteroid, pos):
            self.dragging = True
            self.target = "asteroid"
            self.request_drag.emit(self.target, pos.x() + self.drag_offset_x, pos.y() + self.drag_offset_y)

    def mouseMoveEvent(self, event):
        if self.autoriser_interaction:
         if self.dragging:
            pos = event.pos()
            self.request_drag.emit(self.target, pos.x() + self.drag_offset_x, pos.y() + self.drag_offset_y)

    def mouseReleaseEvent(self, event):
        if self.autoriser_interaction:
         self.dragging = False
         self.target = None
         self.request_release.emit()

    def _hit(self, body, mouse_pos):
        body_pos = self.scaled_point(body.position)
        dx = mouse_pos.x() - body_pos.x()
        dy = mouse_pos.y() - body_pos.y()
        radius_px = int(body.nb_terres * 5)
        return dx*dx + dy*dy <= radius_px*radius_px
    def changer_autoriser_interaction(self,valeur):
        self.autoriser_interaction = valeur

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Animation()
#     window.show()
#     sys.exit(app.exec())

