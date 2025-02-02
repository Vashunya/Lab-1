def temperature(F):
    C = (5 / 9) * (F - 32)
    return C

a = temperature(72)
print(f"From F to C: {a}°")