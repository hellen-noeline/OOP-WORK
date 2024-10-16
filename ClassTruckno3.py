class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f'This vehicle is {self.color}'

class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        return f'{super().toString()}\nHas trailer: {self.has_trailer}'

# Creating a Truck instance
my_truck = Truck('green', True)

# Printing the details of the truck using toString()
print(my_truck.toString())