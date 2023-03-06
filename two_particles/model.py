from config import dt, H, s, e, m
from object import Particle
from random import randint
import math

def calculate_boost(obj, particles):
    obj.ax = 0
    obj.ay = 0
    obj.az = 0
    for part in particles:
        if part != obj:
            x = part.x - obj.x
            y = part.y - obj.y
            z = part.z - obj.z
            r = (x**2 + y**2 + z**2)**0.5
            k = 24 * e / m * (s**6 / r**7 - 2*s**12 / r**13)
            obj.ax += k * x / r
            obj.ay += k * y / r
            obj.az += k * z / r

def calculate_boost_tel(obj, particles):
    for part in particles:
        if part != obj:
            if part.x - obj.x > H/2:
                part.xt = part.x - H
            if part.x - obj.x < - H/2:
                part.xt = part.x + H
            if part.x - obj.x < H/2 and part.x - obj.x > -H/2:
                part.xt = part.x

            if part.y - obj.y > H/2:
                part.yt = part.y - H
            if part.y - obj.y < - H/2:
                part.yt = part.y + H
            if part.y - obj.y < H/2 and part.y - obj.y > -H/2:
                part.yt = part.y

            if part.z - obj.z > H/2:
                part.zt = part.z - H
            if part.z - obj.z < - H/2:
                part.zt = part.z + H
            if part.z - obj.z < H/2 and part.z - obj.z > -H/2:
                part.zt = part.z                        
    obj.ax = 0
    obj.ay = 0
    obj.az = 0
    for part in particles:
        if part != obj:
            x = part.xt - obj.x
            y = part.yt - obj.y
            z = part.zt - obj.z
            r = (x**2 + y**2 + z**2)**0.5
            k = 24 * e / m * (s**6 / r**7 - 2*s**12 / r**13)
            obj.ax += k * x / r
            obj.ay += k * y / r
            obj.az += k * z / r
    
            

def move(particles):
    for obj in particles:
        calculate_boost(obj, particles)
        obj.ax1 = obj.ax
        obj.ay1 = obj.ay
        obj.az1 = obj.az
        # посчитали ускорения частиц
    for obj in particles:
        obj.x = obj.x + obj.vx * dt + 1/2 * obj.ax1 * dt ** 2
        obj.y = obj.y + obj.vy * dt + 1/2 * obj.ay1 * dt ** 2
        obj.z = obj.z + obj.vz * dt + 1/2 * obj.az1 * dt ** 2
        # пересчитали координаты частиц
    for obj in particles:
        calculate_boost(obj, particles)
        obj.vx = obj.vx + 1/2 * (obj.ax1 + obj.ax) * dt
        obj.vy = obj.vy + 1/2 * (obj.ay1 + obj.ay) * dt
        obj.vz = obj.vz + 1/2 * (obj.az1 + obj.az) * dt
        #пересчитали скорости частиц

def move_tel(particles):
    for obj in particles:
        calculate_boost_tel(obj, particles)
        obj.ax1 = obj.ax
        obj.ay1 = obj.ay
        obj.az1 = obj.az
        # посчитали ускорения частиц
    for obj in particles:
        obj.x = obj.x + obj.vx * dt + 1/2 * obj.ax1 * dt ** 2
        obj.y = obj.y + obj.vy * dt + 1/2 * obj.ay1 * dt ** 2
        obj.z = obj.z + obj.vz * dt + 1/2 * obj.az1 * dt ** 2
        # пересчитали координаты частиц
    for obj in particles:
        calculate_boost_tel(obj, particles)
        obj.vx = obj.vx + 1/2 * (obj.ax1 + obj.ax) * dt
        obj.vy = obj.vy + 1/2 * (obj.ay1 + obj.ay) * dt
        obj.vz = obj.vz + 1/2 * (obj.az1 + obj.az) * dt
        #пересчитали скорости частиц   

    for obj in particles:
        if obj.x > H/2:
            obj.x -= H
        if obj.x < -H/2:
            obj.x += H
        if obj.y > H/2:
            obj.y -= H
        if obj.y < -H/2:
            obj.y += H
        if obj.z > H/2:
            obj.z -= H
        if obj.z < -H/2:
            obj.z += H

def generate_particles(n, particles, H): #двумерный случай
    for i in range(n):
        for j in range(n):
            part = Particle()
            part.x = -0.4 * H + 0.8 * H * i / (n - 1)
            part.y = -0.4 * H + 0.8 * H * j / (n - 1)
            angle = randint(0, 360)
            v = 20
            part.vx = v * math.cos(angle * math.pi/180)
            part.vy = v * math.sin(angle * math.pi/180)
            particles.append(part)