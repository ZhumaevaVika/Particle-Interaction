from config import s, e, m, dt, SCALE, X, Y, Z
def calculate_boost(obj, particles):
    obj.ax = 0
    obj.ay = 0
    obj.az = 0
    for part in particles:
        if part != obj:
            x = (part.x - obj.x)*SCALE
            y = (part.y - obj.y)*SCALE
            z = (part.z - obj.z)*SCALE
            r = (x**2 + y**2 + z**2) ** 1/2
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
        # пересчитали скорости частиц

#столкновение со стенками
#    for obj in particles:
#        if (obj.x > X) or (obj.x < 0):
#            obj.vx *= -1
#        if (obj.y > Y) or (obj.y < 0):
#            obj.vy *= -1
#        if (obj.x > Z) or (obj.x < 0):
#            obj.vz *= -1

#телепортация
#    for obj in particles:
#        if obj.x > X:
#            obj.x -= X+80
#        if obj.x < 0:
#            obj.x += X+80
#        if obj.y > Y:
#            obj.y -= Y+80
#        if obj.y < 0:
#            obj.y += Y+80
#        if obj.z > Z:
#            obj.z -= Z+80
#        if obj.z < 0:
#            obj.z += Z+80
        