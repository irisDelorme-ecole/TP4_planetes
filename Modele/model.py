import pymunk as pk
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QPainter, QColor


class Model(QObject):

    conts_grav = (6.674*(10**-11))

    def __init__(self):
        QObject.__init__(self)
        self.space = pk.Space()
        self.space.gravity = (0, -900)



        self.asteroid = pk.Body(300, pk.moment_for_circle(300, 0, 4))

        self.shape = pk.Circle(self.asteroid, 4)

        self.space.add(self.asteroid, self.shape)

        self.planete = pk.Body(1000, pk.moment_for_circle(1000, 0, 10))

        self.shape_planete = pk.Circle(self.planete, 10)

        self.planete.position = (200, 300)

        self.space.add(self.planete, self.shape_planete)


        for step in range(10):
            self.space.step(1/60)
            self.asteroid.apply_force_at_local_point(self.gravity())
            print(f"step {step} pos {self.asteroid.position} v {self.asteroid.velocity}")

    def gravity(self):
        distsqurd = self.planete.position.get_distance_squared(self.asteroid.position)

        pos_asteroid = (self.asteroid.position.x, self.asteroid.position.y)

        pos_planete = (self.planete.position.x, self.planete.position.y)

        dir_f = [pos_planete[i]-pos_asteroid[i] for i in range(2)]

        f = [float(dir_f[i]*((self.conts_grav*self.planete.mass*self.asteroid.mass)/distsqurd)) for i in range(2)]

        return f





if __name__ == "__main__":
    app = Model()