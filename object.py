import pygame as pg
import math
from random import randint
from config import BLUE, X, Y, Z, WIDTH, HEIGHT


class Particle:

    def __init__(self):
        self.m = 1
        self.x = randint(0, X)
        self.y = randint(0, Y)
        self.z = 0
        self.angle = randint(0, 360)
        self.v = 50
        self.vx = self.v * math.cos(self.angle * math.pi/180)
        self.vy = self.v * math.sin(self.angle * math.pi/180)
        self.vz = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.ax1 = 0
        self.ay1 = 0
        self.az1 = 0
        self.r = 10
        self.pos = (self.x, self.y)

    def draw_particle(self, screen):
        self.pos = (self.x * WIDTH / X, self.y * HEIGHT / Y)
        pg.draw.circle(screen, BLUE, self.pos, self.r)




def generate_coordinate(particles, number):
    big_number = (math.ceil(number**0.5))**2
    a = (X*Y/big_number)**0.5
    x0 = a/2
    y0 = a/2
    for obj in particles:
        obj.x = x0
        obj.y = y0
        x0 += a
        if x0 > a*math.ceil(number**0.5):
            y0 += a
            x0 = a/2

def generate_two_particles(particles):
    part1 = Particle()
    part1.vx = 0
    part1.vy = 0
    part1.vz = 0
    part1.x = -0.621
    part1.y = 0
    part1.z = 0
    part2 = Particle()
    part2.vx = 0
    part2.vy = 0
    part2.vz = 0
    part2.x = 0.621
    part2.y = 0
    part2.z = 0
    particles.append(part1)
    particles.append(part2)
    return particles

def draw_two_particles(particles, screen):
    part1 = particles[0]
    part2 = particles[1]
    part1.pos = (part1.x * 10 + 300, part1.y * 10 + 300)
    part2.pos = (part2.x * 10 + 300, part2.y * 10 + 300)
    pg.draw.circle(screen, BLUE, part1.pos, part1.r)
    pg.draw.circle(screen, BLUE, part2.pos, part2.r)



def generate(particles, number):
    for i in range(number):
        part = Particle()
        particles.append(part)
    generate_coordinate(particles, number)
    return particles

