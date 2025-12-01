import sys

from PyQt6.QtWidgets import QApplication

from Controller.controller import Controller
from Modele.model import Model
from Vue.Animation import Animation
from Vue.Vue import Vue

if __name__ == "__main__":
    app = QApplication(sys.argv)
    anim = Animation()
    window = Vue(anim)
    model = Model()
    controller = Controller(model, window, anim)
    window.show()
    sys.exit(app.exec())