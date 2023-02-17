import pygame as pg
from random import randint
from config import BLUE, X, Y, Z


class Particle:

    def __init__(self):
        self.m = 1
        self.x = randint(0, X*1e10)/1e10
        self.y = randint(0, Y*1e10)/1e10
        self.z = randint(0, Z*1e10)/1e10
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.ax1 = 0
        self.ay1 = 0
        self.az1 = 0
        self.r = 10
        self.pos = (self.x, self.y, self.z)

    def draw_particle(self, screen):
        pg.draw.circle(screen, BLUE, self.pos, self.r)


def generate(particles, number):
    for i in range(number):
        part = Particle()
        particles.append(part)
    return particles

