#16) Define a class Vehicle with attributes make and model, and a method drive() which prints
#"Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides
#the drive() method to print "Driving the [make] [model] car".

class Vehicle:
    def __init__(initialization, make, model):
        initialization.make = make
        initialization.model = model
    
    def drive(initialization):
        print(f"Driving the {initialization.make} {initialization.model}")


class Car(Vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} car")


vehicle  = Vehicle("Toyota", "fortuner")
vehicle.drive()

car = Car("tata", "nano")
car.drive()