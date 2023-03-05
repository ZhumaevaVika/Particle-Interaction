import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def calculate_energy(particles):
    E = 0
    for obj in particles:
        v2 = obj.vx**2
        E += 1 * v2/2 #считаем кинетическую энергию
        for part in particles:
            if obj != part:
                x = part.x - obj.x
                y = part.y - obj.y
                z = part.z - obj.z
                r = (x**2 + y**2 + z**2)**0.5
                E += 1/2 * 4 * 1 * ((1/r) ** 12 - (1/r) ** 6) # считаем потенциал взаимодействия частиц
    return E   

def graph(graph_time, graph_energy, graph_R):
    plt.scatter(graph_time, graph_R, s=0.2)
    plt.xlabel("time")
    plt.ylabel("R")
    plt.show()

    plt.scatter(graph_time, graph_energy, s=0.2)
    plt.ylabel("energy")
    plt.xlabel("time")
    plt.show()