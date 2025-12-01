import sys

from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QComboBox
from PyQt6.uic import loadUi


class Vue(QMainWindow):

    canvas : QVBoxLayout
    animation : QVBoxLayout
    corpsComboBox : QComboBox
    


    def __init__(self):
        super().__init__()
        loadUi("ui/tp4.fenetre.ui", self)
        self.show()



    def PaintEvent(self, event):
        pass

    def init_simulation(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vue()
    window.show()
    sys.exit(app.exec())