import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Input degree: "))

radians = degrees_to_radians(degrees)

print(f"Output radian: {radians:.6f}")
