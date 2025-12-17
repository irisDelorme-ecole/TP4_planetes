import numpy as np
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Canvas(QWidget):
    Canvas1: QWidget
    Canvas2: QWidget
    Canvas3: QWidget

    def __init__(self):
        super().__init__()
        self.fig = plt.figure()

        self.canvas1 = Canvas1()
        self.canvas2 = Canvas2()
        self.canvas3 = Canvas3()


"""
celui-ci est quelque peu underwhelming, peut-etre qu<on devrait reconsiderer
"""
class Canvas1(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [], )
        self.ax.set_title("Vitesse vectorielle asteroid")

    def update_vitesse(self, vitesse):
       # print("Distance entre deux astres Updated")
        self.x_data.append(vitesse[0])
        self.y_data.append(vitesse[1])

        #print(f"timer {self.x_data} distance {self.y_data}")

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.draw()

    def reset(self):
        self.x_data = []
        self.y_data = []
        
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()


        self.draw()

class Canvas2(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [],)
        self.ax.set_title("Distance entre les astres")

    def update_distance(self,t,distance):
       # print("Distance entre deux astres Updated")
        self.x_data.append(t)
        self.y_data.append(distance)

        #print(f"timer {self.x_data} distance {self.y_data}")

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.draw()

    def reset(self):
        self.x_data = []
        self.y_data = []

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.draw()

class Canvas3(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [], )
        self.ax.set_title("Amplitude de la force de gravitation")

    def update_vitesse(self,counter, f):
        # print("Distance entre deux astres Updated")
        self.x_data.append(counter)
        self.y_data.append((f[0]**2 + f[1]**2)**(1/2))
        print()

        # print(f"timer {self.x_data} distance {self.y_data}")

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.draw()

    def reset(self):
        self.x_data = []
        self.y_data = []

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()


        self.draw()