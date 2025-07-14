class Shape:
    def area(self):
        return "Undefined"
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
shapes = [Rectangle(4,5) , Circle(4) , Square(5)]

for shape in shapes:
    print(shape.area())


# polymorphic behaviour for operators.
print(4 + 5 * 2) 
print("Hello " + "World!")
print([1,2,3] + [4,5,6])