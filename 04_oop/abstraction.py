from abc import ABC , abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shapes):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

shapes = [Rectangle(4,5),Circle(6)]

for shape in shapes:
    print("Area: ",shape.area() ,"Perimeter", shape.perimeter())