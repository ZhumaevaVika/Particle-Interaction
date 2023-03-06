import numpy as np
from stats import write_coord, calculate_energy, show_graph
from model import move
from object import generate
from config import dt

t = 0
N = 10
particles = []
generate(particles, N)
graph_time = []
graph_energy = []

open('coords.xyz.txt', 'w').close()
for i in range(1000):
    move(particles, "col")
    write_coord(N, particles)
    t = t + dt
    graph_energy = np.append(graph_energy, calculate_energy(particles))
    graph_time = np.append(graph_time, t)

show_graph(graph_time, graph_energy)
