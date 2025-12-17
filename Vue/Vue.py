from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QSpinBox
from PyQt6.uic import loadUi

from Vue.DonneesCanvas import Canvas1, Canvas2, Canvas3


class Vue(QMainWindow):
    canvas: QVBoxLayout
    animation: QVBoxLayout
    corpsComboBox: QComboBox
    vitesseSpinBox : QSpinBox
    commencerPushButton: QPushButton
    pausePushButton: QPushButton
    deletePushButton: QPushButton
    Canvas1 : QWidget
    Canvas2 : QWidget
    Canvas3 : QWidget

    delete = pyqtSignal()
    p = pyqtSignal()

    def __init__(self, animation):
        super().__init__()
        loadUi("Vue/Ui/tp4.fenetre.ui", self)
        self.show()

        self.pausePushButton.setDisabled(True)
        self.deletePushButton.setDisabled(True)
        self.vitesseSpinBox.valueChanged.connect(self.mettre_a_jour_boutons)
        self.commencerPushButton.clicked.connect(self.commencer_animation)

        self.animation.addWidget(animation)

        self.canvas1 = Canvas1(self)
        self.canvas2 = Canvas2(self)
        self.canvas3 = Canvas3(self)

        QVBoxLayout(self.Canvas1).addWidget(self.canvas1)
        QVBoxLayout(self.Canvas2).addWidget(self.canvas2)
        QVBoxLayout(self.Canvas3).addWidget(self.canvas3)

    def commencer_animation(self):
        self.commencerPushButton.setDisabled(True)
        self.pausePushButton.setDisabled(False)
        self.deletePushButton.setDisabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete and self.deletePushButton.isEnabled():
            self.delete.emit()
            
    def mettre_a_jour_boutons(self):
        self.commencerPushButton.setDisabled(False)

    def set_model_combo_box(self, model):
        self.corpsComboBox.setModel(model)

    def set_controller(self, controller):
        #pourquoi est-ce qu'on connait le controlleur?? -iris
        self.__controller = controller
