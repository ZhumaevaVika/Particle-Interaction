import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from config import dt, T
from model import move
from object import Particle
from stats import calculate_energy

part = Particle()
graph_time = []
graph_energy = []
graph_x = []
t = 0
while t < T:
    move(part)
    print("x: ", part.x)
    calculate_energy(part)
    t += dt
    graph_energy = np.append(graph_energy, calculate_energy(part))
    graph_time = np.append(graph_time, t)
    graph_x = np.append(graph_x, part.x)

plt.plot(graph_time, graph_x)
plt.show()
plt.plot(graph_time, graph_energy)
plt.show()