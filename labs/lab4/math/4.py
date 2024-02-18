import math

def areaOfParall(length, heigth):
    return length * heigth

x = int(input("Length of base: "))
y = int(input("Height of parallelogram: "))

txt = "Expected Output: {}"

print(txt.format(areaOfParall(x, y)))