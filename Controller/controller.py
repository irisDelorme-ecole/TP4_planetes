from PyQt6.QtCore import QTimer


class Controller:
    time_step = 3600*24


    def __init__(self, model, vue, animation):
        self.model = model
        self.vue = vue
        self.animation = animation
        self.vue.set_model_combo_box(self.model.model_planetes)

        #syncro anim - model

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(16)


        self.model.signal_update.connect(self.animation.update_anim)


    def update(self):
        self.model.update(1/60)
        #self.vue.update()
        #self.animation.update_pos()



