from config import dt, H

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
            k = 24 * (1 / r**7 - 2 / r**13)
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



r = 1.2
part1 = Particle()
part1.x = - (r / 2)
part1.y = - (r / 2)
part1.z = 0
part1.vx = 0
part2 = Particle()
part2.x = (r / 2)
part2.y = (r / 2)
part2.z = 0
part3 = Particle()
part3.x = (r / 2)
part3.y = - (r / 2)
part4 = Particle()
part4.x = - (r / 2)
part4.y = (r / 2)
part5  = Particle()
part5.y = -2*r
part5.vy = 3
part5.vx = 0.5

r = 3
part1 = Particle()
part1.x = - (r / 2)
part1.y = 0
part1.z = 0
part1.vx = 0
part2 = Particle()
part2.x = (r / 2)
part2.y = 0
part2.z = 0


r = 1.5
part1 = Particle()
part1.x = - (r / 2)
part1.y = - (r / 2)
part1.vx = 0
part2 = Particle()
part2.x = (r / 2)
part2.y = (r / 2)
part3 = Particle()
part3.vy = 5
part4 = Particle()
part4.x = r
part4.y = -r
part4.vx = 8