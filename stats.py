from config import e, s, m
def calculate_energy(particles):
    E = 0
    for obj in particles:
        v2 = (obj.vx**2 + obj.vy**2 + obj.vz**2)
        E += m * v2/2 #считаем кинетическую энергию
        for part in particles:
            if obj != part:
                x = part.x - obj.x
                y = part.y - obj.y
                z = part.z - obj.z
                r = (x**2 + y**2 + z**2) ** 1/2
                E += 1/2 * 4 * e * ((s/r) ** 12 - (s/r) ** 6) # считаем потенциал взаимодействия частиц
    print(E)

def graph(particles, time, energy):
    pass