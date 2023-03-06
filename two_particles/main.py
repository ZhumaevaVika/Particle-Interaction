import pygame as pg
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from config import dt, T, S, H
from model import move, move_tel, generate_particles
from object import Particle
from stats import calculate_energy, graph, draw, write_coord

pg.init()
screen = pg.display.set_mode((S, S))
clock = pg.time.Clock()
loop = True




particles = []
n = 3
generate_particles(n, particles, H)
graph_time = [0]
graph_energy = [0]
t = 0
E0 = calculate_energy(particles)

while loop:
    screen.fill((255,255,255))
    clock.tick(500)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    move_tel(particles)
    #print("x2: ", part2.x)
    #print("x1: ", part1.x)
    print("E: ", calculate_energy(particles))

    draw(screen, particles)
    
    t += dt
    graph_energy = np.append(graph_energy, calculate_energy(particles))
    graph_time = np.append(graph_time, t)

    write_coord(n**3, particles)

    pg.display.update()

graph(graph_time, graph_energy)
pg.quit()

print("E_max: ", np.max(graph_energy[1:]))
print("E_min: ", np.min(graph_energy[1:]))
print("E0: ", E0)