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

class Canvas1(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.__fig, self.__ax = plt.subplots()
        super().__init__(self.__fig)
        self.plot()

    def plot(self):
        x = np.linspace(0, 12, 100)
        y = np.sin(x)
        self.__ax.plot(x, y)
        self.__ax.set_title("Vitesse")

class Canvas2(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [],)

    def update_distance(self,t,distance):
        print("Distance entre deux astres Updated")
        self.x_data.append(t)
        self.y_data.append(distance)

        print(f"timer {self.x_data} distance {self.y_data}")

        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()

        self.draw()

class Canvas3(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.__fig, self.__ax = plt.subplots()
        super().__init__(self.__fig)
        self.plot()

    def plot(self):
        x = np.linspace(10, 100, 100)
        y = np.sin(x)
        self.__ax.plot(x, y)
        self.__ax.set_title("Acceleration")