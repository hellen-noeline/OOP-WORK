#Creating a class vehicle
# vehicle.py
class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        return f'This vehicle is {self.color}'


# Creating an instance for the vehicle
my_vehicle = Vehicle('red')

# Getting the color of the vehicle
print(my_vehicle.getColor())

# Printing the details of the vehicle using toString()
print(my_vehicle.toString())