

# 1 Creating a Class and Objects----------------------------

class Car(): 
    def __init__(self, brand:str, model:str, year:int, milage:int):# Constructor , # Initializing the attributes of the car class
        
        self.brand = brand
        self.model = model
        self.year = year
        self.milage = milage

    def display_info(self):
        print(f"Car_Brand: {self.brand}")
        print(f"Car_Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Milage: {self.milage}")
    
    # 2 Methods and Object Behavior---------------------------
    # Creating a drive method that takes in a distance and modifies the the mileage

    def drive(self,distance:int):
        self.milage += distance

car1 = Car("Toyota","Supercustom",2003,20000)
car2 = Car("Ford", "Mustang", 2019, 25000)
car3 = Car("Honda", "Civic", 2021, 5000)

print('Car1')
car1.display_info()

print("\n")
print('Car2')
car2.display_info()

print("\n")
print('Car3')
car3.display_info()


car4 = Car("Toyota", "Camry", 2020, 15000)
print('\nCar4 information')
car4.display_info()
car4.drive(100)
print('\nCar4 after driving a distance of 100km')
car4.display_info()



# # 3 Benefits of OOP------------------------------------
# # Class ElectricCar that inherits from the Car class its parent class
class ElectricCar(Car): # ElectricCar class.
    def __init__(self, brand:str, model:str, year:int, milage:int, battery_capacity:int,charge_level:int):
        super().__init__(brand, model, year, milage)

        self.battery_capacity = battery_capacity
        self.charge_level = charge_level

    def charge(self,amount:int):
        self.charge_level += amount
        if self.charge_level > 100:
            self.charge_level = 100
        print(f'The charge level is {self.charge_level}%')


Tesla_1 = ElectricCar("Tesla","Model Y",2023,2000,75,85)

print("\n")
Tesla_1.display_info()
Tesla_1.charge(4)
print("\n")





"""(3c) Write a brief explanation (4-5 sentences) on how the ElectricCar class demonstrates 
the principles of modularity, reusability, and maintainability.

Modularity : ElectricCar inherits from the Car class and this separates common car properties from ElectricCar separate ones. This keeps the code organized and easier to understand

Reusability : By inheriting from the Car class, ElectricCar reuses existing code for displaying car information.This avoids code duplication and promotes efficiency

Maintainability : Adding new electric car features becomes easier. One can simply add new methods specific to electric cars within ElectricCar without modifying the core car functionality in Car

"""




# 4a.  Rewrite the Car functionality (from Task 1) using a procedural programming approach.


def create_car(brand,model,year,mileage):# Function for creating a car object that takes in parameters
    return{
        "brand":brand,
        "model":model,
        "year":year,
        "mileage":mileage
    }

def display_info(car): # Function for displaying the car information
    print(f'Car Brand : {car["brand"]}')
    print(f'Car Model : {car["model"]}')
    print(f'Car Year : {car["year"]}')
    print(f'Car Mileage : {car["mileage"]}')
 

def drive(car,distance):
    car['mileage'] += distance
    print(f'Car has been driven for {distance} km')


car1 = create_car("Toyota", "Camry", 2020, 15000)
print("Car 1 information")
display_info(car1)

print(" ")

"""(4b).
What differences did you notice between the OOP and procedural implementations?

OOP uses encapsulation within objects while procedural programming uses separate entities

Procedural programming doesn't support inheritance while OOP supports inheritance

Procedural programming comprises of functions while OOP comprises of objects

In procedural programming code is typically divided into modules or subroutines while OOP is typically divided into classes and objects"""


"""How does OOP provide benefits like modularity, reusability, and maintainability compared to procedural programming?

OOP has modularity provides encapsulation of data and methods that are used within the class and this creates organized self contained units while procedural programming functions are all separated

OPP enables reusability of methods and attributes like in the case of inheritance a child class is able to reuse the methods and attributes of its parent class while this functionality is no available in procedural programming

OOP provides easier maintainability in terms of modifications ie; changes can be made to specific objects or their methods without affecting the entire program, reducing the risk of unintended side effects while this is not applicable in procedural programming."""





"""5.Assignment Task: StudentManagement class with methods for adding, updating, and 
deleting students, use exception handling where needed. """

class Student_Mgt(): # Class Student Management
    def __init__(self):
        self.students = {} # Dictionary students to store the data of the students added to the system

    def add_student(self, Reg_number:str, student_name:str): # Method for adding students to the system. Takes in two parameters (Reg_number and students name)

        if Reg_number in self.students: # Incase the Reg number entered already exists in the system a ValueError is raised letting the user know the Reg is already there
            raise ValueError("Registration Number already in system")
        self.students[Reg_number] = student_name
        print(f'Student {student_name} added with Registration Number {Reg_number}')

    def update_student(self,Reg_number,updated_name):
        if Reg_number not in self.students: # Incase the Reg number entered does not in the system a KeyError letting the user know that the Key does not exist within the dictionary
            raise KeyError('Registration number is not in system')
        self.students[Reg_number] = updated_name
        print(f'Name updated to {updated_name} for Registration number {Reg_number}')

    def delete_student(self,Reg_number):

        if Reg_number not in self.students:
            raise KeyError('Registration number is not in system') # Incase the Reg number entered does not in the system a KeyError letting the user know that the Key does not exist within the dictionary
        removed = self.students.pop(Reg_number)
        print(f'{removed} with Registration number {Reg_number} was removed from the System')

    def display_students(self):

        if not self.students:
            print("No students in System")
            return
        for Reg_number, student_name in self.students.items():
            print(f"Name : {student_name}, RegNo : {Reg_number}")

System = Student_Mgt()

try:

    System.add_student("M23B23/016","Arthur")

    System.update_student("M23B23/016",'Yawe')




except (ValueError,KeyError) as e:
    print(f'Error : {e}')