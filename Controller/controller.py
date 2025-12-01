import sys

from PyQt6.QtWidgets import QApplication

from Vue.Vue import Vue

import Modele.model as Model
from Vue.Animation import Animation


class Controller:

    def __init__(self, model, vue, animation):
        self.model = model
        self.vue = vue
        self.animation = animation

        #syncro anim - model
        self.model.signal_update.connect(self.update)

    def update(self, pos_asteroid):
        #self.vue.update()
        self.animation.update(self.flip_pymunk_to_qt(600,pos_asteroid))

    def flip_pymunk_to_qt(self, height, position):
        return position[0], position[1]-height

