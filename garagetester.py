class Vehicle:
    def __init__(self, color):
        self.color = color

    def toString(self):
        return f'This vehicle is {self.color}'


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


class GarageTester:
    def getExample():
        # Creating a black Truck without a trailer
        black_truck = Truck('black', has_trailer=False)

        # Creating a Garage instance
        my_garage = Garage()

        # Parking the Truck in the Garage
        my_garage.setVehicle(black_truck)

        return my_garage


# Testing the GarageTester class
example_garage = GarageTester.getExample()
print(example_garage.toString())