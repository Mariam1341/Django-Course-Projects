import math


class Circle:
    def __init__(self, radius = 10):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return 2 * math.pi * self.radius

cir1 = Circle()
print('defalt radius:')
print('Area:',cir1.getArea(),'Circumference:',cir1.getCircumference())

cir2 = Circle(5)
print()
print('without defalt radius:')
print('Area:',cir2.getArea(),'Circumference:',cir2.getCircumference())