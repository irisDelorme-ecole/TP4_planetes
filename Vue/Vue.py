import os
from faulthandler import is_enabled

from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QSpinBox
from PyQt6.uic import loadUi


class Vue(QMainWindow):
    canvas: QVBoxLayout
    animation: QVBoxLayout
    corpsComboBox: QComboBox
    vitesseSpinBox: QSpinBox
    commencerPushButton: QPushButton
    pausePushButton: QPushButton
    deletePushButton: QPushButton

    def __init__(self, animation):
        super().__init__()
        loadUi("Vue/Ui/tp4.fenetre.ui", self)
        self.show()
        self.is_started = False
        # self.commencerPushButton.setDisabled(True)
        # self.pausePushButton.setDisabled(True)
        # self.deletePushButton.setDisabled(True)
        self.vitesseSpinBox.valueChanged.connect(self.mettre_a_jour_boutons)
        self.commencerPushButton.clicked.connect(self.commencer_animation)
        self.deletePushButton.clicked.connect(self.gestion_pauses)

        self.animation.addWidget(animation)

    def gestion_pauses(self):
        self.pausePushButton.setEnabled(True)

    def commencer_animation(self):
        self.commencerPushButton.setDisabled(False)
        self.is_started = True
        self.gestion_pauses()
        self.deletePushButton.setDisabled(False)

    def mettre_a_jour_boutons(self):
        # besoin d'un validator
        if self.vitesseSpinBox.value() == 0:
            self.commencerPushButton.setDisabled(True)
        else:
            self.commencerPushButton.setDisabled(False)

    def set_model_combo_box(self, model):
        self.corpsComboBox.setModel(model)

    def set_controller(self, controller):
        self.__controller = controller
