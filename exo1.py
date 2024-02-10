import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**5

# valeurs pour x
x_curve = np.linspace(0, 1, 1000)
x_points = np.random.rand(1000) 

# valeurs pour y 
y_points = np.random.rand(1000)

# Tracer la courbe
plt.plot(x_curve, f(x_curve) + 0.5, 'r')

# Ajouter les points en dessous et au dessus de la courbe
for i in range(len(x_points)):
    if y_points[i] > f(x_points[i]) + 0.5:
        # Point au-dessus de la courbe en bleu
        plt.plot(x_points[i], y_points[i], 'bo')  
    else:
        # Point en dessous de la courbe en vert
        plt.plot(x_points[i], y_points[i], 'go')  

# Droites limite le carré
plt.plot([0, 1], [0, 0], 'b') 
plt.plot([0, 1], [1, 1], 'b') 
plt.plot([0, 0], [0, 1], 'b') 
plt.plot([1, 1], [0, 1], 'b') 

# Limites des axes
plt.xlim(-0.1, 1.1)
plt.ylim(0, 1.6)


# Afficher la grille
plt.grid(True)

# Afficher le graphique
plt.show()
