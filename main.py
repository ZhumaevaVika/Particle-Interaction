import pygame as pg
from config import FPS, WIDTH, HEIGHT, WHITE
from object import generate

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
loop = True

balls = []
generate(balls, 2)

while loop:
    screen.fill(WHITE)
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    for ball in balls:
        ball.move()
        ball.draw_particle(screen)

    pg.display.update()

pg.quit()
