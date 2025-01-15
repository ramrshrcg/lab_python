#14) Write a Python program to create a class representing a Circle. Include methods to calculate its area
#and perimeter
# class circle:
#     radius=2
# PI=2.14
    

# area= 2*PI*circle.radius*circle.radius

# print(f'the area of circle is {area} ')

# perimeter= PI*circle.radius
# print(f'the perimeter of circle is {perimeter} ')
import math

class Circle:
    def __init__(self, radius):
       
        self.radius = radius

    def calculate_area(self):
       return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area of the circle: {circle.calculate_area():.2f}")
print(f"Perimeter of the circle: {circle.calculate_perimeter():.2f}")

