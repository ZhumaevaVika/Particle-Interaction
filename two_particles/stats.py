def calculate_energy(obj):
    E = obj.vx ** 2 + 4 * (1/(2*obj.x)**12 - 1/(2*obj.x)**6)
    return E