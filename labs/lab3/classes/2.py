class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
    



myShape = Shape()
print(myShape.area())

square = Square(10)
print(square.area())