import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.radius


circy = Circle(15)
print(circy.getArea())  

circy = Circle(4.85)
print(circy.getPerimeter())  
