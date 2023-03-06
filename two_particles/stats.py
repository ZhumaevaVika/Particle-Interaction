import pygame as pg
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from config import K, S, H, m, e, s

def calculate_energy(particles):
    E = 0
    for obj in particles:
        v2 = obj.vx**2 + obj.vy**2 + obj.vz**2
        E += 1 * m * v2/2 #считаем кинетическую энергию
        for part in particles:
            if obj != part:
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

                x = part.xt - obj.x
                y = part.yt - obj.y
                z = part.zt - obj.z
                r = (x**2 + y**2 + z**2)**0.5
                E += 1/2 * 4 * e * ((s/r) ** 12 - (s/r) ** 6) # считаем потенциал взаимодействия частиц
    return E   

def graph(graph_time, graph_energy):
    #plt.scatter(graph_time, graph_R, s=0.2)
    #plt.xlabel("time")
    #plt.ylabel("R")
    #plt.show()

    plt.scatter(graph_time, graph_energy, s=0.2)
    plt.ylabel("energy")
    plt.xlabel("time")
    plt.show()

def draw(screen, particles):
    for part in particles:
        part.pos = (K * part.x + S/2, K * part.y + S/2)
        pg.draw.circle(screen, (0,0,1), part.pos, K/2)