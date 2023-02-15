import pygame as pg
from random import randint
from config import BLUE


class Particle:

    def __init__(self):
        self.m = 1
        self.x = randint(100, 200)
        self.y = randint(100, 200)
        self.z = 0
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.vz = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.r = 10
        self.pos = (self.x, self.y)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.pos = (self.x, self.y)

    def draw_particle(self, screen):
        pg.draw.circle(screen, BLUE, self.pos, self.r)


def generate(balls, number):
    for i in range(number):
        ball = Particle()
        balls.append(ball)
    return balls

