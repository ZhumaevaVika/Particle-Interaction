import pygame as pg
import numpy as np
from config import FPS, WIDTH, HEIGHT, WHITE, dt, N
from object import generate
from model import move
from stats import calculate_energy, show_graph

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
loop = True

t = 0
graph_time = []
graph_energy = []

particles = []
generate(particles, N) 
while loop:
    screen.fill(WHITE)
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    for part in particles:
        part.draw_particle(screen)
    move(particles)
    t = t + dt
    graph_energy = np.append(graph_energy, calculate_energy(particles))
    graph_time = np.append(graph_time, t)
    pg.display.update()

show_graph(graph_time, graph_energy)
pg.quit()
