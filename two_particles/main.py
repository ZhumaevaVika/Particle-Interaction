import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from config import dt, T
from model import move
from object import Particle
from stats import calculate_energy, graph

r = 1.1 * (2**0.5)
part1 = Particle()
part1.x = - (r / 2) / (2**0.5)
#part1.y = - (r / 2) / (2**0.5)
part2 = Particle()
part2.x = (r / 2) / (2**0.5)
#part2.y = (r / 2) / (2**0.5)
particles = [part1, part2]
graph_time = [0]
graph_energy = [0]
graph_R = [0]
t = 0
E0 = calculate_energy(particles)

while t < T:
    move(particles)
    #print("x2: ", part2.x)
    #print("x1: ", part1.x)
    print("E: ", calculate_energy(particles))
    t += dt
    R = ((part2.x - part1.x)**2 + (part2.y - part1.y)**2 + (part2.z - part1.z)**2)**0.5
    graph_energy = np.append(graph_energy, calculate_energy(particles))
    graph_time = np.append(graph_time, t)
    graph_R = np.append(graph_R, R)

graph(graph_time, graph_energy, graph_R)

print("E_max: ", np.max(graph_energy[1:]))
print("E_min: ", np.min(graph_energy[1:]))
print("E0: ", E0)