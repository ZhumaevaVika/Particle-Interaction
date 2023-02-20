import numpy as np
from config import e, s, m
import matplotlib
from matplotlib import pyplot as plt


def calculate_energy(particles):
    E = 0
    for obj in particles:
        v2 = (obj.vx**2 + obj.vy**2 + obj.vz**2)
        E += m * v2/2 #считаем кинетическую энергию
        for part in particles:
            if obj != part:
                x = part.x - obj.x
                y = part.y - obj.y
                z = part.z - obj.z
                r = (x**2 + y**2 + z**2) ** 1/2
                E += 1/2 * 4 * e * ((s/r) ** 12 - (s/r) ** 6) # считаем потенциал взаимодействия частиц
    return E


def show_graph(graph_time, graph_energy):
    plt.plot(graph_time, graph_energy)
    plt.show()


def write_coord(N, particles):
    file = open("coords.xyz.txt", "a")
    n_str = str(N)
    file.write(n_str + '\n \n')
    for obj in particles:
        file.write('H ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.z) + ' \n')

    file.close()
