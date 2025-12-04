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


class Planete:
    _masse: float
    _couleur: QColor
    _rayon: float
    _nom: str

    def __init__(self, masse, rayon, nom, couleur):
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
    conts_grav = (6.674 * (10 ** -11))
    H = 400
    W = 800
    #1 pixel = 1km?


    signal_update = pyqtSignal(object)
    _list_planetes = [Planete(33011e19, 2440000, "Mercure", "darkGray"),
                      Planete(4867500000000000000000000, 6052000, "Venus", "darkYellow"),
                      Planete(5970000000000000000000000, 6371000, "Terre", "blue"),
                      Planete(641710000000000000000000, 3390000, "Mars", "darkRed"),
                      Planete(1898000000000000000000000000000, 69911000, "Jupiter", "white"),
                      Planete(568300000000000000000000000000, 58232000, "Saturne", "Yellow"),
                      Planete(86810000000000000000000000000, 25362000, "Uranus", "green"),
                      Planete(102400000000000000000000000000, 24622000, "Neptune", "darkBlue")]
    model_planetes : QAbstractListModel


    def __init__(self):
        QObject.__init__(self)
        self.space = pk.Space()
        self.space.gravity = (0,0)
        self.model_planetes = PlanetesListModel(self._list_planetes)





        # par souci de clarté, screen = 400 x 500
        # tests pour comprendre
        self.asteroid = pk.Body(30000, pk.moment_for_circle(3000, 0, 4))

        self.shape = pk.Circle(self.asteroid, 4)



        self.planete = pk.Body(1e17,pk.moment_for_circle(1e17, 0, 10))

        self.shape_planete = pk.Circle(self.planete, 10)

        self.planete.position = (600, 200)

        self.asteroid.position = (50, 50)

        self.space.add(self.planete, self.shape_planete)
        self.space.add(self.asteroid, self.shape)

        # for step in range(100):
        #     self.space.step(1 / 60)
        #


    def update(self, dt: float):
        self.space.step(dt)
        f = self.gravity_on_asteroid()
        self.asteroid.apply_impulse_at_local_point(f)

        print("pos planete : ", self.planete.position)
        self.signal_update.emit(self.asteroid)
        print(self.asteroid.position)

    """
    devrait retourner la force gravitationnelle sur l'asteroide
    """

    def gravity_on_asteroid(self):
        distsqurd = self.planete.position.get_distance_squared(self.asteroid.position)

        pos_asteroid = (self.asteroid.position.x, self.asteroid.position.y)

        pos_planete = (self.planete.position.x, self.planete.position.y)


        dir_f = [(pos_planete[i] - pos_asteroid[i])/distsqurd**(1/2) for i in range(2)]


        f = [float(dir_f[i] * ((self.conts_grav * self.planete.mass * self.asteroid.mass) / distsqurd)) for i in
             range(2)]

        print(f)
        return f



    @property
    def list_planetes(self):
        return self._list_planetes


if __name__ == "__main__":
    model = Model()
