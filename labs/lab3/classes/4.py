class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, xmove, ymove):
        self.x += xmove
        self.y += ymove

        return self.x, self.y

    def dist(self, point2):
        distance = ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
        return distance


myPoint1 = Point(7, 6)
myPoint2 = Point(10, 8)


print(Point.dist(myPoint1, myPoint2))
