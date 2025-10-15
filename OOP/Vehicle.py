"""
Polymorphism Examples
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        return "Moving"

class Car(Vehicle):
    pass

class Boat(Vehicle):
    #overriding move method in vehicle
    def move(self):
        return "Sailing"

class Plane(Vehicle):
    #overriding move method in vehicle
    def move(self):
        return "Flying"

c1 = Car("Toyota", "Corolla")
b1 = Boat("Yamaha", "242X")
p1 = Plane("Boeing", "747")

for v in (c1, b1, p1):
    print(f"{v.brand} {v.model}: {v.move()}")

