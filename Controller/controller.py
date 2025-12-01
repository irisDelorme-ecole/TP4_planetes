from PyQt6.QtCore import QTimer


class Controller:

    def __init__(self, model, vue, animation):
        self.model = model
        self.vue = vue
        self.animation = animation

        #syncro anim - model

        timer = QTimer()
        timer.timeout.connect(self.update)
        timer.start(16)


    def update(self):
        self.model.update()
        #self.vue.update()
        #self.animation.update_pos()

    def flip_pymunk_to_qt(self, height, position):
        return int(position[0]), int(position[1]-height)

