import os

from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QComboBox, QLineEdit, QPushButton
from PyQt6.uic import loadUi


class Vue(QMainWindow):

    canvas : QVBoxLayout
    animation : QVBoxLayout
    corpsComboBox : QComboBox
    vitesseLineEdit : QLineEdit
    commencerPushButton : QPushButton
    pausePushButton : QPushButton
    deletePushButton : QPushButton
    


    def __init__(self, animation):
        super().__init__()
        loadUi("Vue/Ui/tp4.fenetre.ui", self)
        self.show()

        self.animation.addWidget(animation)



    def set_model_combo_box(self, model):
        self.corpsComboBox.setModel(model)
    def set_controller(self, controller):
        self.__controller = controller



