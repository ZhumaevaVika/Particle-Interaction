import pygame as pg
from config import FPS, WIDTH, HEIGHT, WHITE, dt
from object import generate
from model import move 

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
loop = True
t = 0

particles = []
generate(particles, 2)

while loop:
    screen.fill(WHITE)
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    for part in particles:
        part.draw_particle(screen)
    move(particles, dt)
    t = t + dt
    pg.display.update()

pg.quit()
