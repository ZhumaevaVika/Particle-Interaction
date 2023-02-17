from config import dt
from object import generate
from model import move 
from stats import calculate_energy

particles = []
generate(particles, 50)
t = 0

while t < 1:
    move(particles, dt)
    t += dt
    calculate_energy(particles)