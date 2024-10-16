class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f'This vehicle is {self.color}'

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def toString(self):
        return f'{super().toString()}\nHas winter tires: {self.has_winter_tires}'

# Creating a Car instance
my_car = Car('pink', True)

# Printing the details of the car using toString()
print(my_car.toString())