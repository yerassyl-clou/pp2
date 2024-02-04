class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.wigth = width
    
    def area(self):
        return self.length * self.wigth
    

rect = Rectangle(3, 4)
print(rect.area())
