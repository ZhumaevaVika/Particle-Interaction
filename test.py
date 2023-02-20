from stats import write_coord
from model import move
from object import generate
from config import dt

t = 0
N = 2
particles = []
generate(particles, N)

open('coords.xyz.txt', 'w').close()
for i in range(1000):
    move(particles)
    write_coord(N, particles)
    t += dt
