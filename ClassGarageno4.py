
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


class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        return f'{super().toString()}\nHas trailer attached: {self.has_trailer}'


class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def setVehicle(self, parked):
        if isinstance(parked, Vehicle):
            self.parked_vehicle = parked
        else:
            print("Invalid vehicle type. Only Vehicles are allowed in the garage.")

    def toString(self):
        if self.parked_vehicle:
            return f'Description of the parked vehicle...\n{self.parked_vehicle.toString()}'
        else:
            return 'The garage is empty.'

# Testing the Garage class


my_garage = Garage()

my_car = Car('yellow', True)
my_truck = Truck('green', False)

my_garage.setVehicle(my_car)
print(my_garage.toString())

my_garage.setVehicle(my_truck)
print(my_garage.toString())        