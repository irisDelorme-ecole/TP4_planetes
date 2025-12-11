import pymunk as pk
from PyQt6.QtCore import QObject, pyqtSignal, QAbstractListModel, Qt, QModelIndex
from PyQt6.QtGui import QColor
import numpy as np


class PlanetesListModel(QAbstractListModel):
    def __init__(self, data):
        super().__init__()
        self.__planetes = data or []


    def data(self, index, role):
        if not index.isValid():
            return None
        planete = self.__planetes[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return planete.__str__()
        elif role == Qt.ItemDataRole.UserRole:
            return planete
        return None

    def get_planetes(self, index):
        return self.__planetes[index]

    def rowCount(self, parent=QModelIndex()):
        return len(self.__planetes)


class Planete(pk.Body): #derrive de body pour stocker pos
    _masse: float
    _couleur: QColor
    _rayon: float
    _nom: str

    def __init__(self, masse, rayon, nom, couleur, nb_terres):
        super().__init__(masse, pk.moment_for_circle(masse, 0, rayon))
        self.masse = masse
        self.rayon = rayon
        self.couleur = couleur
        self.nom = nom
        self.nb_terres = nb_terres

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def masse(self):
        return self._masse

    @masse.setter
    def masse(self, masse):
        self._masse = masse

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, rayon):
        self._rayon = rayon

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, couleur):
        self._couleur = couleur
    def __str__(self):
        return self._nom


class Model(QObject):
    G = 6.674e-11#help it works but i cant get the scale right..... keeps launching into the void
    H = 800
    W = 1000

    signal_update = pyqtSignal(object, object)
    #rayons en km
    _list_planetes = [Planete(3.3e23, 2440, "Mercure", "darkGray", 0.4),
                      Planete(4.8e24, 6052, "Venus", "darkYellow", 0.9),
                      Planete(6e24, 6371, "Terre", "blue", 1),
                      Planete(6.42e23, 3390, "Mars", "darkRed", 0.5),
                      Planete(1.9e27, 69911, "Jupiter", "white", 11),
                      Planete(5.7e26, 58232, "Saturne", "Yellow", 9.1),
                      Planete(8.7e25, 25362, "Uranus", "green", 4),
                      Planete(1e28, 24622, "Neptune", "darkBlue" , 3.9)]
    model_planetes : PlanetesListModel

    SCALE =500 / (0.5e8)

    def __init__(self, asteroid, planete):
        QObject.__init__(self)
        self.space = pk.Space()
        self.model_planetes = PlanetesListModel(self._list_planetes)
        self.__asteroid = asteroid
        self.planete = planete





        # tests pour comprendre (on espere avoir un scale correct bientot.)
        self.shape = pk.Circle(self.__asteroid, int(self.__asteroid.rayon))


        self.__asteroid.velocity = (10 / self.SCALE, 20 / self.SCALE)


        self.shape_planete = pk.Circle(self.planete, int(self.planete.rayon))

        self.planete.position = (750/self.SCALE, 500/self.SCALE)
        self.__asteroid.position = (self.planete.position.x - 600 / self.SCALE,
                                    self.planete.position.y - 150 / self.SCALE)

        self.__asteroid.position = (self.planete.position.x-600/self.SCALE, self.planete.position.y-150/self.SCALE)

        self.__asteroid.velocity = (10/self.SCALE, 20/self.SCALE)

        self.shape.elasticity = 10
        self.shape_planete.elasticity = 10

        self.space.add(self.planete, self.shape_planete)
        self.space.add(self.__asteroid, self.shape)

    @property
    def asteroid(self):
        return self.asteroid

    @asteroid.setter
    def asteroid(self, asteroid):
        self.space.remove(self.__asteroid)
        self.__asteroid = asteroid
        self.shape = pk.Circle(self.__asteroid, int(self.__asteroid.rayon))
        self.__asteroid.position = (self.planete.position.x - 600 / self.SCALE,
                                  self.planete.position.y - 150 / self.SCALE)

        self.__asteroid.velocity = (10 / self.SCALE, 20 / self.SCALE)
        self.space.add(self.__asteroid, self.shape)
        print(self.__asteroid)


    def set_vitesse(self, value):
        self.__asteroid.velocity = ((np.sqrt((value**2)/5))/self.SCALE, 2*(np.sqrt((value**2)/5))/self.SCALE)

    def update(self, dt: float):
        self.space.step(dt)
        f = self.gravity_on_asteroid()
        self.__asteroid.apply_impulse_at_local_point(f)

        f2 = self.gravity_on_planet()
        print(f2, "                 FORCE")
        self.planete.apply_impulse_at_local_point(f2)
        print("pos planete : ", self.planete.position)
        self.signal_update.emit(self.__asteroid, self.planete)
        print(self.__asteroid.position)

    """
    devrait retourner la force gravitationnelle sur l'asteroide
    """

    def gravity_on_asteroid(self):
        distsqurd = self.planete.position.get_distance_squared(self.__asteroid.position)

        x_a = self.__asteroid.position.x
        y_a = self.__asteroid.position.y

        x_p = self.planete.position.x
        y_p = self.planete.position.y



        dir_f = [(x_p -x_a) / (distsqurd**(1/2)), (y_p -y_a) / (distsqurd**(1/2))]


        f = [float(dir_f[i] * ((self.G * self.planete.mass * self.__asteroid.mass) / distsqurd)) for i in
             range(2)]

        print(f)
        return f

    def gravity_on_planet(self):
        distsqurd = self.planete.position.get_distance_squared(self.__asteroid.position)

        x_a = self.__asteroid.position.x
        y_a = self.__asteroid.position.y

        x_p = self.planete.position.x
        y_p = self.planete.position.y

        dir_f = [(x_a - x_p) / (distsqurd ** (1 / 2)), (y_a - y_p) / (distsqurd ** (1 / 2))]

        f = [float(dir_f[i] * ((self.G * self.planete.mass * self.__asteroid.mass) / distsqurd)) for i in
             range(2)]

        print(f)
        return f


    @property
    def list_planetes(self):
        return self._list_planetes


