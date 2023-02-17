from config import dt
from object import generate
from model import move 
from stats import calculate_energy

particles = []
generate(particles, 10)
t = 0

while t < 1:
    move(particles)
    t += dt
    calculate_energy(particles)