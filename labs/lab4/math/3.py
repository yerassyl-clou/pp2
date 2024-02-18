import math
from functions import degTorad

def areaOfPolygon(sides, length):
    perimetr = sides * length
    ap = (length / (2 * math.tan(degTorad(180/sides))))

    return (perimetr * ap) / 2

x = int(input("Input number of sides: "))
y = int(input("Input the length of a side: "))

txt = "The area of the polygon is: {}"
print(txt.format(round(areaOfPolygon(x,y), 1)))
