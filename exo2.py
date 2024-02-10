import matplotlib.pyplot as plt
import numpy as np

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def _f(self, x):
        return x**5

    def plot_curve(self):
        x_curve = np.linspace(self.start, self.stop, 1000)
        plt.plot(x_curve, self._f(x_curve) + 0.5, 'r')

    def determine_position(self, x, y):
        if y > self._f(x) + 0.5:
            return 'above'
        else:
            return 'below'

    def generate_points(self):
        x_points = np.random.rand(self.nbr_points)
        y_points = np.random.rand(self.nbr_points)

        surface_bleu = 0
        surface_verte = 0

        for i in range(len(x_points)):
            if self.determine_position(x_points[i], y_points[i]) == 'above':
                plt.plot(x_points[i], y_points[i], 'bo')
                surface_bleu += 1
            else:
                plt.plot(x_points[i], y_points[i], 'go')
                surface_verte += 1

        surface_bleu /= self.nbr_points
        surface_verte /= self.nbr_points

        surface_bleu *= (self.stop - self.start) * 1.6
        surface_verte *= (self.stop - self.start) * 1.6

        return surface_bleu, surface_verte

    def plot_square_boundaries(self):
        plt.plot([self.start, self.stop], [0, 0], 'b')
        plt.plot([self.start, self.stop], [1, 1], 'b')
        plt.plot([self.start, self.start], [0, 1], 'b')
        plt.plot([self.stop, self.stop], [0, 1], 'b')

        plt.xlim(self.start - 0.1, self.stop + 0.1)
        plt.ylim(0, 1.6)

        plt.grid(True)
        plt.show()

# Utilisation de la classe
curve = Curve(0, 1)
curve.plot_curve()
surface_bleu, surface_verte = curve.generate_points()
print("Surface en bleu:", surface_bleu)
print("Surface en vert:", surface_verte)
curve.plot_square_boundaries()
