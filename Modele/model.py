import pymunk as pk
from PyQt6.QtCore import QObject


class Model(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.space = pk.Space()


        self.asteroid = pk.Body(300, pk.moment_for_circle(300, 0, 4))

        self.shape = pk.Circle(self.asteroid, 4)

        self.space.add(self.asteroid, self.shape)

        self.asteroid.apply_impulse_at_local_point((10,10), (0,0))

        for step in range(10):
            self.space.step(1/60)
            print(f"step {step} pos {self.asteroid.position}")

if __name__ == "__main__":
    app = Model()