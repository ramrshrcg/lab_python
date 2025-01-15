# 19) Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
# methods start() and stop(). The Car class should have instances of Engine and Wheel classes
# as attributes. Implement a method start_car() in the Car class which starts the engine and prints
# "Car started".

class Engiene:
    def __init__(self, type):
        self.type = type
        

    def start(self):
        print("car engiene started")
    
    def stop(self):
        print("car engiene stopped")



class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print("car wheel start")
    
    def stop(self):
        print("car wheel stop")



class Car:
    def __init__(self, engine, wheel):
        self.engine =Engiene(engine)
        self.wheel = Wheel(wheel)

    def startCar(self):
        self.engine.start()
        self.wheel.start()
        print("Car started")
    
    def stopcar(self):
        self.engine.stop()
        self.wheel.stop()
        print("Car started")


my_car = Car("Petrol", "tubeless")
my_car.startCar()
my_car.stopcar()