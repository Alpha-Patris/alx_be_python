import math
class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length:float, width:float):
        assert length > 0, f"{length} should be larger than 0."
        assert width > 0, f"{width} should be larger than 0."
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius:float):
        assert radius > 0, f"{radius} should be larger than 0."
        self.radius = radius
        

    def area(self):
        return math.pi * (self.radius ** 2)    