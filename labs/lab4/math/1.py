import math

def degTorad(degrees):
    radians = math.pi / 180 * degrees
    return radians

x = int(input("Input degree: "))
print("Output radian: " + str(degTorad(x)))