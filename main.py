import sys
import traceback

from PyQt6.QtWidgets import QApplication

from Controller.controller import Controller
from Modele.model import Model
from Vue.Animation import Animation
from Vue.Vue import Vue

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

sys.excepthook = qt_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    anim = Animation()
    window = Vue(anim)
    model = Model()
    controller = Controller(model, window, anim)
    window.set_controller(controller)
    window.show()
    sys.exit(app.exec())