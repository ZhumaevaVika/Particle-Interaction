from config import dt

def calculate_boost(obj):
    obj.ax = 24 * (1 / (2 * obj.x) ** 7 - 2 / (2 * obj.x) ** 13) * -1

def move(obj):
    calculate_boost(obj)
    obj.ax1 = obj.ax
    # посчитали ускорения частиц

    obj.x = obj.x + obj.vx * dt + 1/2 * obj.ax1 * dt ** 2
    # пересчитали координаты частиц

    calculate_boost(obj)
    obj.vx = obj.vx + 1/2 * (obj.ax1 + obj.ax) * dt
 