from PyQt6.QtCore import QTimer


class Controller:



    def __init__(self, model, vue, animation):
        self.model = model
        self.vue = vue
        self.animation = animation
        self.vue.set_model_combo_box(self.model.model_planetes)

        #syncro anim - model

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)
        self.timer.stop()

        self.model.set_canvases(self.vue.canvas1, self.vue.canvas2, self.vue.canvas3)

        self.vue.vitesseSpinBox.valueChanged.connect(self.set_vitesse)

        self.vue.pausePushButton.clicked.connect(self.stop)
        self.vue.pausePushButton.clicked.connect(self.stop)
        self.vue.commencerPushButton.clicked.connect(self.start)
        self.vue.corpsComboBox.currentIndexChanged.connect(self.change_asteroid)


        self.model.signal_update.connect(self.animation.update_anim)

        # self.vue.deletePushButton.clicked.connect(self.reset)

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
        self.model.update_graph()
        #self.vue.update()
        #self.animation.update_pos()



