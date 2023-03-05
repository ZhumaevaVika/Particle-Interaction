from config import dt

def calculate_boost(obj, particles):
    obj.ax = 0
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
 