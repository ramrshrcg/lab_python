# '''#18) Implement a class Shape with a method area() which returns 0. Then, create subclasses
# Rectangle and Circle. Overload the area() method in both subclasses to calculate and return
# the area of a rectangle and a circle respectively'''

class Shape:
   
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)
    
area=Rectangle(10,5).area()
print(f"area of rectangle is {area}")

area=Circle(5)
areaofcircle = area.area()
print(f"area of circle is {areaofcircle}")
