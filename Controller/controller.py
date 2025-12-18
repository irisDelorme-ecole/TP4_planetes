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

        self.set_canvases(self.vue.canvas1, self.vue.canvas2, self.vue.canvas3)
        self.model.dist_updated.connect(self.canvas2.update_distance)

        self.vue.vitesseSpinBox.valueChanged.connect(self.set_vitesse)

        self.vue.pausePushButton.clicked.connect(self.gestion_pause)
        self.vue.commencerPushButton.clicked.connect(self.start)
        self.vue.corpsComboBox.currentIndexChanged.connect(self.change_asteroid)
        self.vue.deletePushButton.clicked.connect(self.reset)
        self.vue.delete.connect(self.reset)
        self.vue.p.connect(self.gestion_pause)


        self.model.signal_update.connect(self.update_views)

        self.animation.request_drag.connect(self.on_drag)
        self.animation.request_release.connect(self.on_release)

    def on_drag(self, target, x, y):
        if self.timer.isActive():
            self.timer.stop()

        self.model.move_body(target, x, y)

    def on_release(self):
        self.timer.start(16)

    def reset(self):
        self.timer.stop()
        self.model.initiatlize_anim(self.model.asteroid, self.model.planete)
        self.model.counter = 0
        self.reset_canvases()
        self.animation.update_anim(self.model.asteroid, self.model.planete)
        self.vue.commencerPushButton.setEnabled(True)
        self.vue.deletePushButton.setEnabled(False)
        self.vue.pausePushButton.setEnabled(False)

    def reset_canvases(self):
        self.canvas1.reset()
        self.canvas2.reset()
        self.canvas3.reset()

    def update_views(self):
        self.animation.update_anim(self.model.asteroid, self.model.planete)
        self.canvas2.update_distance(self.model.counter, self.model.distance)
        self.canvas1.update_vitesse(self.model.asteroid.velocity)
        self.canvas3.update_vitesse(self.model.counter,self.model.f_asteroid)

    def set_canvases(self, canvas1, canvas2, canvas3):
        self.canvas1 = canvas1
        self.canvas2 = canvas2
        self.canvas3 = canvas3

    def gestion_pause(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.start()

    def change_asteroid(self, index):
        self.model.asteroid = self.model.model_planetes.get_planetes(index)
        self.reset()

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
        #self.model.update_graph()
        #self.vue.update()
        #self.animation.update_pos()



