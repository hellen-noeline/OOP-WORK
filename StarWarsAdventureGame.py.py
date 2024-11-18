import random 

# Character class 
class Character:
    def __init__(self, name, health, position):
        self._name = name  # Encapsulation: private attribute
        self._health = health  # Encapsulation: private attribute
        self._position = position  # Encapsulation: private attribute
    
    def move(self, new_position):  # Abstraction: allows movement functionality
        self._position = new_position
        print(f"{self._name} has moved to {self._position}")
    
    @property
    def attack(self):  # Abstraction: Attacking logic is hidden
        self._health -= 10  # Decreases health by 10 on attack
        print(f"{self._name} attacks and takes damage! Health decreases to {self._health}")
    
    def interact(self, obj):  # Interacting with objects/items
        print(f"{self._name} is interacting with {obj}")

    def get_in(self, vehicle):  # Abstraction: Getting in the vehicle
        vehicle_name = vehicle.vehicle_type
        return f"{self._name} gets in the {vehicle_name}"
    
    def get_out(self, vehicle):  # Abstraction: Getting out of the vehicle
        vehicle_type = vehicle.vehicle_type
        return f"{self._name} gets out of the {vehicle_type}"

    def Enter_vehicle(self, vehicle): 
        print(self.get_in(vehicle))  # Uses get_in method to simplify interaction with the vehicle

    def Exit_vehicle(self, vehicle):  
        print(self.get_out(vehicle))  # Uses get_out method to simplify interaction with the vehicle

    @property
    def name(self):  # Getter (encapsulation)
        return self._name

    @property
    def health(self):  # Getter (encapsulation)
        return self._health

# Vehicle class
class Vehicle:
    def __init__(self, vehicle_type, speed, fuel_level, position=(0, 0)):
        self._vehicle_type = vehicle_type  # Encapsulation: private attribute
        self._speed = speed  # Encapsulation: private attribute
        self._fuel_level = fuel_level  # Encapsulation: private attribute
        self._position = position  # Encapsulation: private attribute
    
    @property
    def drive(self):  # Driving the vehicle
        if self._fuel_level > 0:
            self._fuel_level -= 10  # Reduces fuel level by 10
            print(f"The {self._vehicle_type} is being driven.")
        else:
            print(f"The {self._vehicle_type} is out of fuel.")

    def refuel(self, amount):  # Refueling the vehicle
        self._fuel_level += amount  # Increases fuel level by amount
        if self._fuel_level > 1000:
            self._fuel_level = 1000
            print(f"The {self._vehicle_type} was refueled by {amount}")
        else:
            print(f"The {self._vehicle_type} was refueled by {amount}")

    @property
    def stop(self):  # Stopping the vehicle
        print(f"The {self._vehicle_type} has stopped.")

    @property
    def vehicle_type(self):  # Getter (encapsulation)
        return self._vehicle_type

# HeroCharacter 
class HeroCharacter(Character):
    def __init__(self, name, health, position):
        super().__init__(name, health, position)  # Inheritance

    @property
    def double_jump(self):  # Polymorphism: Special hero action (double jump)
        print(f"{self._name} performs a double jump!")
    
    @property
    def fast_run(self):  # Polymorphism: Special hero action (fast run)
        print(f"{self._name} runs very fast!")

# Interacting with vehicle (Polymorphism)
def using_vehicle(vehicle, character):
    character.Enter_vehicle(vehicle) 
    vehicle.drive  
    vehicle.stop 
    character.Exit_vehicle(vehicle)  


# Creating a game scenario (Using all pillars)
def game_scenario(vehicle, HeroCharacter):
    print("\n🎮🎮🎮🎮🎮🎮STAR WARS UNDERWORLD ARCHITECT🎮🎮🎮🎮🎮🎮\n")
    print("")
    print("YOUR ARE A MEMBER OF THE STAR WARS ARCITECT AND YOUR MISSION IS TO PROTECT OUTPOSTS FROM REBELS THROUGHOUT THE CITY")
    print("")
    HeroCharacter.interact("pistol")
    print("")
    print(f"{HeroCharacter.name} gets her pistol")
    print("")
    HeroCharacter.move((2,5))
    print("")
    print("Enter your car and drive to chase after the rebel")
    print("")
    HeroCharacter.Enter_vehicle(vehicle)
    print("")
    vehicle.drive  
    print("")
    vehicle.stop  
    print("")
    HeroCharacter.Exit_vehicle(vehicle)
    print("")
    HeroCharacter.fast_run  
    print("")
    HeroCharacter.double_jump  
    print("")
    print(f"\n{HeroCharacter.name} has caught up to the rebel now stop him using your weapon\n")
    print("")
    attacks = random.randint(1,12)
    for attack in range(attacks):
        HeroCharacter.attack  
    if HeroCharacter.health <= 0:
        print("")
        print("MISSION FAILED: You were killed by the rebel")
    else:
        print("")
        print("MISSION COMPLETE: THE REBEL IS DOWN")
    

# IMPLEMENTATION
# Object for class Character
character1 = Character("Hellen", 21, (0, 0))

character1.move((2, 10))
character1.attack  
character1.interact("baton") 
print("---------------------------------------")

# Object for class Vehicle
vehicle1 = Vehicle("Ford Mustang", 200, 0)

vehicle1.drive  
vehicle1.refuel(500)  
vehicle1.stop  
print("----------------------------------------")

using_vehicle(vehicle1, character1)  # Using vehicle functionality
print("----------------------------------------")

# Object for class HeroCharacter (Hero inherits from Character)
hero1 = HeroCharacter("The Mandalorian", 100, (0, 0))
hero1.double_jump  
hero1.fast_run  
print("----------------------------------------")

# Main game scenario (including Hero and Vehicle)
cop = HeroCharacter("Hellen", 100, (0, 0))
copCar = Vehicle("Ford Mustang", 200, 50)
game_scenario(copCar, cop)  # Running the game scenario
