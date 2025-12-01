
import pymunk as pk
from PyQt6.QtCore import QObject, pyqtSignal

class Model(QObject):


    conts_grav = (6.674*(10**-11))
    signal_update = pyqtSignal(object)


    def __init__(self):
        QObject.__init__(self)
        self.space = pk.Space()

        self.W, self.H = 600, 400



        #tests pour comprendre
        self.asteroid = pk.Body(3, pk.moment_for_circle(3, 0, 30))

        self.shape = pk.Circle(self.asteroid, 4)

        self.space.add(self.asteroid, self.shape)

        self.planete = pk.Body(10000000000000, pk.moment_for_circle(10000000000000, 0, 90), body_type = pk.Body.STATIC)

        self.shape_planete = pk.Circle(self.planete, 10)

        self.planete.position = (200, 300)

        self.space.add(self.planete, self.shape_planete)




    def step(self, dt:float):
        self.space.step(dt)
        self.asteroid.apply_force_at_local_point(self.gravity())
        self.signal_update.emit(self.asteroid)


    """
    devrait retourner la force gravitationnelle sur l'asteroide
    """
    def gravity(self):
        distsqurd = self.planete.position.get_distance_squared(self.asteroid.position)

        pos_asteroid = (self.asteroid.position.x, self.asteroid.position.y)

        pos_planete = (self.planete.position.x, self.planete.position.y)

        dir_f = [pos_planete[i]-pos_asteroid[i] for i in range(2)]

        f = [float(dir_f[i]*((self.conts_grav*self.planete.mass*self.asteroid.mass)/distsqurd)) for i in range(2)]

        return f





if __name__ == "__main__":
    model = Model()

