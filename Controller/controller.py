from PyQt6.QtCore import QTimer, QThread, pyqtSignal, Qt, QModelIndex

from Modele.model import Model, PlanetesListModel


class Controller:


    def __init__(self, model, vue, animation):
        self.model = model
        self.vue = vue
        self.animation = animation
        self.vue.set_model_combo_box(self.model.model_planetes)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)
        self.timer.stop()
        #syncro anim - model

        self.update()

        self.model.signal_update.connect(self.animation.update_anim)
        self.vue.vitesseSpinBox.valueChanged.connect(self.set_vitesse)

        self.vue.pausePushButton.clicked.connect(self.stop)
        self.vue.pausePushButton.clicked.connect(self.stop)
        self.vue.commencerPushButton.clicked.connect(self.start)
        self.vue.corpsComboBox.currentIndexChanged.connect(self.change_asteroid)
        #self.vue.deletePushButton.clicked.connect(self.reset)

    def change_asteroid(self, index):
        self.model.asteroid = self.model.model_planetes.get_planetes(index)

    # def  reset(self):
    #     self.model =Model(self.vue.corpsComboBox.currentText())

    def start(self):
        self.timer.start(16)

    def stop(self):
        self.timer.stop()

    def set_vitesse(self, value):
        self.model.set_vitesse(int(value))


    def update(self):
        self.model.update(10/60)
        #self.vue.update()
        #self.animation.update_pos()





