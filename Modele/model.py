import pymunk as pk
from PyQt6.QtCore import QObject, pyqtSignal, QAbstractListModel, Qt, QModelIndex
from PyQt6.QtGui import QColor


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
    def rowCount(self, parent=QModelIndex()):
        return len(self.__planetes)


class Planete(pk.Body): #derrive de body pour stocker pos
    _masse: float
    _couleur: QColor
    _rayon: float
    _nom: str

    def __init__(self, masse, rayon, nom, couleur):
        super().__init__(masse, pk.moment_for_circle(masse, 0, rayon))
        self.masse = masse
        self.rayon = rayon
        self.couleur = couleur
        self.nom = nom

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
    H = 600
    W = 800

    signal_update = pyqtSignal(object, object)
    #rayons en km
    _list_planetes = [Planete(33011e13, 2440, "Mercure", "darkGray"),
                      Planete(4867500000000000000, 6052, "Venus", "darkYellow"),
                      Planete(5970000000000000000, 6371, "Terre", "blue"),
                      Planete(641710000000000000, 3390, "Mars", "darkRed"),
                      Planete(1898000000000000000000, 69911, "Jupiter", "white"),
                      Planete(568300000000000000000000, 58232, "Saturne", "Yellow"),
                      Planete(86810000000000000000000, 25362, "Uranus", "green"),
                      Planete(102400000000000000000000, 24622, "Neptune", "darkBlue")]
    model_planetes : QAbstractListModel


    def __init__(self):
        QObject.__init__(self)
        self.space = pk.Space()
        self.space.gravity = (0,0)
        self.model_planetes = PlanetesListModel(self._list_planetes)





        # tests pour comprendre (on espere avoir un scale correct bientot.)
        self.planete = Planete(568300000000000000000000, 58.232, "Saturne", "Yellow")
        self.asteroid = Planete(33011e13, 24.40, "Mercure", "darkGray")

        self.shape = pk.Circle(self.asteroid, int(self.asteroid.rayon))


        self.shape_planete = pk.Circle(self.planete, int(self.planete.rayon))

        self.planete.position = (600, 300)

        self.asteroid.position = (50, 50)

        self.space.add(self.planete, self.shape_planete)
        self.space.add(self.asteroid, self.shape)


    def update(self, dt: float):
        self.space.step(dt)
        f = self.gravity_on_asteroid()
        self.asteroid.apply_impulse_at_local_point(f)

        f2 = self.gravity_on_planet()
        self.planete.apply_force_at_local_point(f2)
        print("pos planete : ", self.planete.position)
        self.signal_update.emit(self.asteroid, self.planete)
        print(self.asteroid.position)

    """
    devrait retourner la force gravitationnelle sur l'asteroide
    """

    def gravity_on_asteroid(self):
        distsqurd = self.planete.position.get_distance_squared(self.asteroid.position)

        pos_asteroid = (self.asteroid.position.x, self.asteroid.position.y)

        pos_planete = (self.planete.position.x, self.planete.position.y)


        dir_f = [(pos_planete[i] - pos_asteroid[i])/distsqurd**(1/2) for i in range(2)]


        f = [float(dir_f[i] * ((self.G * self.planete.mass * self.asteroid.mass) / distsqurd)) for i in
             range(2)]

        print(f)
        return f

    def gravity_on_planet(self):
        distsqurd = self.planete.position.get_distance_squared(self.asteroid.position)

        pos_asteroid = (self.asteroid.position.x, self.asteroid.position.y)

        pos_planete = (self.planete.position.x, self.planete.position.y)


        dir_f = [(pos_asteroid[i]- pos_planete[i])/distsqurd**(1/2) for i in range(2)]


        f = [float(dir_f[i] * ((self.G * self.planete.mass * self.asteroid.mass) / distsqurd)) for i in
             range(2)]

        print(f)
        return f


    @property
    def list_planetes(self):
        return self._list_planetes


if __name__ == "__main__":
    model = Model()
