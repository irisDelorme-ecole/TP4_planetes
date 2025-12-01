import os

from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QComboBox
from PyQt6.uic import loadUi


class Vue(QMainWindow):

    canvas : QVBoxLayout
    animation : QVBoxLayout
    corpsComboBox : QComboBox
    


    def __init__(self, animation):
        super().__init__()
        loadUi("Vue/Ui/tp4.fenetre.ui", self)
        self.show()

        self.animation.addWidget(animation)







