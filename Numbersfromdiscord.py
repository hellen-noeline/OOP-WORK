#Number 1a
class Person:
 def __init__(self,name,age,gender):
    self.name= name
    self.age= age
    self.gender= gender

#number 1aii
class Employee(Person):
    def __init__(self,name,age,gender,employee_id,department):
        super().__init__(name,age,gender)
        self.employee_id= employee_id
        self.department= department
        self.tasks=[]

 #b)       
    def assign_task(self,task):
        if task in self.tasks:
            print(f"The Task {task} has been assigned")
        else:
            self.tasks.append(task)
            print(f"The Task {task} has been assigned to{self.name}")

 #display employee_info
    def display_employee_info(self):
       print(f"{self.name} in {self.department} has been assigned to{self.tasks}")  

#c)Creating employee objects        
employee_1=Employee("Hellen",20,"Female","E001","Computing")        
employee_2=Employee("Mark",21,"Male","E002","Engineering")

#assign tasks
employee_1.assign_task("Mark papers")
employee_2.assign_task("Build project")

print(f"Employee 1 who is {employee_1.name} in {employee_1.department} has been assigned to {employee_1.tasks}")
print(f"Employee 1 who is {employee_2.name} in {employee_2.department} has been assigned to {employee_2.tasks}")

#display employee_info
def display_employee_info(self):
    print(f"{self.name} in{self.department} has been assigned to{self.tasks}")

# d)Displaying their information
employee_1.display_employee_info()
employee_2.display_employee_info()


#Question 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        # Pass only the arguments expected by Vehicle
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  # Car-specific attribute
        self.fuel_level = 0  # Initialize fuel level to 0

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Refueled {amount} liters. Current fuel level: {self.fuel_level} liters.")

    def display_vehicle_info(self):
        print(f"Make: {self.make}, Model: {self.model} ,Year: {self.year}, "
              f"Fuel Type: {self.fuel_type} ,Fuel Level: {self.fuel_level} liters")

car1 = Car("Toyota", "Corolla", 2020, "Petrol")

# Display initial info
car1.display_vehicle_info()

# Refuel and display updated info
car1.refuel(20)
car1.display_vehicle_info()

class Car(Vehicle):
    # Other methods remain unchanged
    
    def refuel(self, amount, tank_capacity=50):
        if self.fuel_level + amount > tank_capacity:
            print(f"Cannot refuel beyond tank capacity of {tank_capacity} liters.")
        else:
            self.fuel_level += amount
            print(f"Car refueled. Current fuel level: {self.fuel_level} liters.")

# Display initial vehicle info
car1.display_vehicle_info()

# Attempt to refuel with valid and excess amounts
car1.refuel(30)  # Within capacity
car1.refuel(25)  # Exceeds capacity
car1.display_vehicle_info()

#question 3
class ShopItem:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class Electronics(ShopItem):
    def __init__(self, name, price, stock_quantity, warranty_period):
        # Pass only the arguments expected by ShopItem
        super().__init__(name, price, stock_quantity)
        self.warranty_period = warranty_period  # Electronics-specific attribute

    def sell_item(self, quantity):
        if quantity > self.stock_quantity:
            print(f"Cannot sell {quantity} units. Only {self.stock_quantity} in stock.")
        elif quantity <= 0:
            print("Quantity must be greater than zero.")
        else:
            self.stock_quantity -= quantity
            print(f"Sold {quantity} units of {self.name}. {self.stock_quantity} left.")

    def display_item_info(self):
        print(f"Item: {self.name}, Price: ${self.price}, Stock: {self.stock_quantity}, Warranty: {self.warranty_period}")

item1 = Electronics("Laptop", 1000, 10, "2 years")
item2 = Electronics("Smartphone", 700, 5, "1 year")

# Display initial info
item1.display_item_info()
item2.display_item_info()

# Sell items
item1.sell_item(3)
item2.sell_item(6)  # Exceeds stock

# Display updated info
item1.display_item_info()
item2.display_item_info()

#question4


#question 20
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")



from abc import ABC, abstractmethod
# # Question 1
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# class Employee(Person):
#     def __init__(self,name,age,gender,employee_id,department):
#         super().__init__(name,age,gender)
#         self.employee_id = employee_id
#         self.department = department
#         self.tasks =[]

#     def assign_task(self,task):
    
#         if task in self.tasks:
#             print("Task already assigned")
#         else:
#             self.tasks.append(task)
#         return self.tasks
   
#     def display_employee_info(self):
#         return{
#             "Name" : self.name,
#             "Department": self.department,
#             "Tasks" :self.tasks
#         }


# # Creating objects of employee
# Employee1 = Employee("Lynn",21,"Female",1002,"ICT")
# Employee2 = Employee("Amoit",21,"Female",1003,"ICT")

# print(Employee1.assign_task("Directing"))
# print()
# print(Employee1.assign_task("Auditing"))
# print()
# print(Employee1.assign_task("Auditing"))
# print()

# print("EMPLOYEE INFORMATION AND TASKS")
# print(f" name:{Employee1.name}\n age:{Employee1.age}\n gender:{Employee1.gender}\n employee_id:{Employee1.employee_id}\n department:{Employee1.department}")
# print(f"{Employee1.name} is assigned to {Employee1.tasks}")


# print()

# print(Employee1.display_employee_info())
# print()
# # print(Employee2.display_employee_info())

# QUESTION TWO
# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make 
#         self.model = model
#         self.year = year

# class Car(Vehicle):
#     fuel_level = 50
#     def __init__(self, make, model, year,fuel_type):
#         super().__init__(make,model,year)
#         self.fuel_type = fuel_type

#     def refuel(self,amount):
#         if self.fuel_level + amount > 100:
#             print("Tank capacity exceeded")
#             self.fuel_level = 100
#             print(f"Fuel_level has been set to {self.fuel_level}")
#         else: 
#          self.fuel_level += amount
#          print(f"The fuel has been increased to {self.fuel_level}")

#     def driving(self):
#         return (f"The {self.make} is being driven")
    
#     def display_vehicle_info(self):
#         print(f"Make:{self.make}\n Model:{self.model}\n Year:{self.year}\n fuel_level:{self.fuel_level}")

# Car1 = Car("Rolls Royce", "Toyota" , 2001 ,"Petrol")
# print(Car1.driving())
# Car1.display_vehicle_info()
# Car1.refuel(20)
# print(Car1.fuel_level)


# Question 3
# class ShopItem:
#     stock_quantity = 100
#     def __init__(self,name,price,stock_quantity):
#         self.name = name
#         self.price = price
#         self.stock_quantity = stock_quantity

# class Electronic(ShopItem):
#     def __init__(self, name, price, stock_quantity, warranty_period):
#         super().__init__(name, price, stock_quantity)
#         self.warranty_period = warranty_period

#     def sell_item(self, quantity):
        
#         if self.stock_quantity == 0:
#             print("Out of stock")

#         elif quantity > self.stock_quantity:
#             print("The quantity requested is less in stock")

#         else:
#            self.stock_quantity -= quantity
#            print(f"The current stock of {self.name}s is {self.stock_quantity}")

#     def display_item_info(self):
#         print(f"Name:{self.name}\n Price:{self.price}\n Stock_Quantity:{self.stock_quantity}\n Warranty_Period:{self.warranty_period}")

# Electronic1 = Electronic("mouse", 15000, 10, 1)
# Electronic2 = Electronic("keyboards",100000, 30, 1)

# Electronic1.display_item_info()
# Electronic1.sell_item(12)

# Question 4
# class Author:
#     def __init__(self,name,nationality):
#         self.name = name
#         self.nationality = nationality

# class Book(Author):
#     def __init__(self, name, nationality,title,genre):
#         super().__init__(name, nationality)
#         self.title = title
#         self.genre = genre
#         self.availability = True

#     def borrow_book(self):
#         if self.availability:
#             print(f"{self.title} has been borrowed")
#             self.availability = False
#         else:
#             print("Book is unavailable")
    
#     def display_Book_info(self):
#         print(f" Book_Title:{self.title}\n Author:{self.name}\n Availability_Status:{self.availability}")



# Book1 = Book("Jane K","British","Pride and Prejudice","Romance")
# Book1.display_Book_info()
# Book1.borrow_book()
# Book1.borrow_book()

# Question 5
# class Animal:
#     def __init__(self,species,name,habitat):
#         self.species = species
#         self.name = name
#         self.habitat = habitat

# class Mammal(Animal):
#     def __init__(self, species, name, habitat, fur_color):
#         super().__init__(species, name, habitat)
#         self.fur_color = fur_color
#         self.animal_state = 'Not fed'


#     def feed(self):
#         if self.animal_state == "Not fed":
#             self.animal_state = 'fed'
#             print(f"The {self.name} has been {self.animal_state}") 
#         elif self.animal_state == "fed":
#             print("Animal has been fed")
    
#     def display_animal_info(self):
#         print(f" Species:{self.species}\n Name:{self.name}\n Current_state:{self.animal_state}")

# Mammal1 = Mammal("Anty","Cow" ,"Kraal","Brown")
# Mammal2 = Mammal("Anty","Dog" ,"Kennel", "Black")

# Mammal1.display_animal_info()
# Mammal1.feed()
# Mammal1.feed()
# Mammal1.display_animal_info()

# Question 6
# class BankAccount:
#     def __init__(self,account_number,balance,account_holder):
#         self.account_number = account_number
#         self.balance = balance
#         self.account_holder = account_holder

# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance, account_holder,interest_rate):
#         super().__init__(account_number, balance, account_holder)
#         self.interest_rate = interest_rate
        

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"The {self.account_number} has been deposited with {amount}shs")
#         print(f"Your new balance is {self.balance}shs")
        
    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Balance is insufficient")
        
#         elif amount == self.balance:
#             self.balance = 0
#             print(f"Your balance is now {self.balance}")
        
#         else:
#             self.balance -= amount
#             print(f"{self.account_holder} has withdrawn {self.amount} from her account")

#     def display_Account_info(self):
#         print(f" Account_number:{self.account_number}\n Balance:{self.balance}\n Account_holder:{self.account_holder}\n Interest_Rate:{self.interest_rate}")

# SavingsAccount1 = SavingsAccount("B20813", 100, "Lynn" ,0.5)
# SavingsAccount1.withdraw(1000)
# SavingsAccount1.display_Account_info()
# SavingsAccount1.withdraw("100000shs")


# Question 7
# class Publisher:
#     def __init__(self,name,location,founded_year):
#         self.name = name
#         self.location = location
#         self.founded_year = founded_year

# class Magazine(Publisher):
#     def __init__(self, name, location, founded_year,issue_number):
#         super().__init__(name, location, founded_year)
#         self.issue_number = issue_number
        
#     def publish(self):
        
#         print(f"{self.name} issue has been published")

#     def display_Magazine_info(self):
#         print(f" Magazine:{self.name}\n Location:{self.location}\n Founded_year:{self.founded_year}\n Issue_number:{self.issue_number}")

# Magazine1 = Magazine("NewVision","Kampala","2002",12)
# Magazine2 = Magazine("Bukedde","Kampala","2004",13)

# Magazine1.publish()
# Magazine2.publish()

# Magazine1.display_Magazine_info()

# Question 8
# class AccountHolder:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# class LoanAccount(AccountHolder):
#     def __init__(self, name, age,address,loan_amount,interest_rate):
#         super().__init__(name, age,address)
#         self.loan_amount = loan_amount
#         self.interest_rate = interest_rate

#     def apply_for_loan(self,amount):
#         self.loan_amount += amount
#         print(f"{self.name} has applied for a loan of {amount}shs")
#         print(f"Current loan amount: {self.loan_amount}")


#     def Repay_loan(self,amount):
#         if amount > self.loan_amount:
#             excess = amount - self.loan_amount
#             print(f"Loan completed and extra money of {excess}shs")
#         else:
#             self.loan_amount -= amount
#             print(f"{self.name}  has made a payment of {amount}shs")
#             print(f"Current loan  amount: {self.loan_amount}")

#     def display_loan_info(self):
#         print(f" name:{self.name}\n age:{self.age}\n address:{self.address}\n loan_amount:{self.loan_amount}\n intrest_rate:{self.interest_rate}")

# LoanAccount1 = LoanAccount("Lynn", 21, "seeta", 20, 0.5)



# print(LoanAccount1.loan_amount)
# # LoanAccount1.apply_for_loan(100)
# LoanAccount1.Repay_loan(120)
# # LoanAccount1.display_loan_info()

#Question 9
# class TeamMember:
#     def __init__(self,name, role, skill_level):
#         self.name = name
#         self.role = role
#         self.skill_level = skill_level

# class Project:
#     def __init__(self,project_name,project_deadline):
#         self.project_name = project_name
#         self.project_deadline = project_deadline
#         self.projet_members = {}

#     def assign_member(self,team_member):
#         if team_member.name in self.projet_members:
#             print("Member already there")
#         else:
#             self.projet_members[team_member.name] = [team_member.role, team_member.skill_level]
#             print("Added")
    
#     def display_project_info(self):
#         return {
#             "Project Name": self.project_name,
#             "Project deadline": self.project_deadline,
#             "Assigned": self.projet_members
#         }


# member1 = TeamMember("Lynn", "Frontend", 5)
# member2 = TeamMember("Arthur", "Backend", 2)

# Project1 = Project("Management System", "27/11/2024")

# Project1.assign_member(member1)
# Project1.assign_member(member2)

# print(Project1.display_project_info())


# Question 10
# class Passenger:
#     def __init__(self,name, ticket_number, seat_number):
#         self.name = name 
#         self.ticket_number = ticket_number
#         self.seat_number = seat_number

# class Flight:
#     def __init__(self, flight_number,destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.passengers = {}

#     def assign_seat(self,passenger):
#         if passenger.seat_number in self.passengers:
#             print("Seat already assigned to a passenger")
#         else:
#             self.passengers[passenger.seat_number] = [passenger.name]
#             print(f"{passenger.name} has been assigned to seatnumber {passenger.seat_number}")

#     def display_flight_info(self):

#         return{
#             "Flight_number": self.flight_number,
#             "Destination": self.destination,
#             "Passengers": self.passengers
#         }

# Flight1 = Flight(1, "Calfornia")
# Passenger1 = Passenger("Arthur", 40, 2)
# Passenger2 = Passenger("Amoit", 43, 3)

# Flight1.assign_seat(Passenger1)
# Flight1.assign_seat(Passenger2)

# print(Flight1.display_flight_info())

# Question 11
# class Customer:
#     def __init__(self,name,email,phone_number):
#         self.name = name
#         self.email = email
#         self.phone_number = phone_number
    

# class Order:
#     def __init__(self,order_number,order_date,status):
#         self.order_number = order_number
#         self.order_date = order_date
#         self.status = status
      
#     def place_order(self,customer):
#          if self.status == "waiting" or self.status == "cancelled":
#             self.status = "Placed"
#             print(f"{customer.name} has placed an order  with order number {self.order_number}")
#          else:
#             print(f"Order{self.order_number} is already {self.status}. Cannot place again.")
    
#     def cancel_order(self,customer):
#           if self.status == "Placed":
#             self.status = "Cancelled"
#             print(f"{customer.name} has cancelled the order")
#           else:
#             print(f"Order {self.order_number} has not been placed")

#     def display_order_details(self,customer):
#       return {
#         "Customer name": {customer.name},
#         "Order number" : {self.order_name},
#         "Order date ":{self.order_date},
#         "status" :{self.status}

#       }

# Customer1 = Customer("Lynn","amoitlynn1@gmail.com",781317468)
# Customer2 = Customer("Amoit","amoit@gmail.com",752688264)

# Order1 = Order(1, "24/9/2024", "waiting")

# # Order1.place_order(Customer1)
# Order1.cancel_order(Customer1)

# Order1.display_order_details(Customer1)

# Question 12
# class Teacher:
#   def __init__(self,name,subject,years_of_experience):
#     self.name = name
#     self.subject = subject
#     self.year_of_experience = years_of_experience

# class Classroom:
#   def __init__(self,class_code):
#     self.class_code = class_code
#     self.student_list = []

#   def add_student(self,student_name):

#     if student_name in self.student_list:
#       print("Student already in list")

#     else:
#       self.student_list.append(student_name)
#       print(f"{student_name} added to list")

#   def removeStudent(self,student_name):
#       if student_name in self.student_list:
#         self.student_list.remove(student_name)
#       else:
#         print(f"{student_name} is not in the student_list")

# Classroom1 = Classroom("p1")
# Classroom1.add_student("Lynn")
# Classroom1.add_student("Lynn")


# Classroom1.removeStudent("Amoit")

# Question 13
# class Doctor:
#   def __init__(self,name,specialization,years_of_experience):
#     self.name = name
#     self.specialization = specialization
#     self.year_of_experience = years_of_experience
#     self.scheduled_appointments = []

# class Appointment:
#   def __init__(self,patient_name,date,status):
#     self.name = patient_name
#     self.date = date 
    
#     self.status = status

#   def schedule_appointment(self,doctor):
#     if self in doctor.scheduled_appointments:
#       print("Appointment has already been made")
#     else:
#       doctor.scheduled_appointments.append(self)
#       print(f"{doctor.name} has been given a {self.name}")
    

#   def cancel_appointment(self, doctor):
#     if self not in doctor.scheduled_appointments:
#       print("The appointment was never made.")
#     else:
#       doctor.scheduled_appointments.remove(self)
#       print(f"{self.name}'s appointment has been cancelled")

#   def __repr__(self):
#     return f"{self.name}"
    
  
# doctor1 = Doctor("Lynn","surgeon", 10)
# appointment1 = Appointment("Promise","24/9/2024","Pending")
# appointment2 = Appointment("Joshua","24/11/2024","Pending")
# appointment3 = Appointment("Nicole","17/10/2024","Pending")

# appointment1.schedule_appointment(doctor1)
# appointment2.schedule_appointment(doctor1)
# appointment3.schedule_appointment(doctor1)

# print(doctor1.scheduled_appointments)

# appointment3.cancel_appointment(doctor1)
# print(doctor1.scheduled_appointments)


 
#  Qyestion 40
# class User(ABC):
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

#     @abstractmethod
#     def login(self):
#         pass
    
# class Admin_User(User):
#     def __init__(self,username,password):
#         super().__init__(username,password)

#     def login(self):
#         global verification_code
#         verification_code = 1234
#         user_input = int(input(f"Please enter the verification code:"))

#         if user_input == verification_code:
#             print("Login successfull")

#         else:
#             print("invalid verification code")

#         User_password = "Lynn22"
#         User_input = input(f"Enter password:")

#         if User_input == User_password:
#             print("Login successfull")

#         else:
#             print("Password incorrect")

#     def edit_content(self):
#         print("Content has been edited")
        
#     def view_content(self):
#         print("This is displaying content")

#     def manage_permissions(self):
#         verification_code = 1234
#         input1 = int(input("Enter verification code:"))
#         if input1 == verification_code:
#             print("You can now manage paermissions")
#         else:
#             print("Incorrect verification code")        

# class Guest_user(User):
#         def __init__(self,username,password):
#             super().__init__(username,password)
        
#         def login(self):
#           User_name = (input("Input user_name"))
#           print(f"welcome {User_name}")

        

# User1 = Guest_user("Leti","98765")
# Admin1 = Admin_User("Lynn","6543")
# User1.login()
# Admin1.manage_permissions()

        
# QUESTION 39
# from abc import ABC, abstractmethod
# class Transport(ABC):
#     def __init__(self,name, capacity):
#         self.name = name
#         self.capacity = capacity

#     @abstractmethod
#     def calculate_speed(self,distance,time):
#         pass
    
# class Bus(Transport):
#     def __init__(self, name, capacity) :
#         super().__init__(name, capacity)
        

#     def calculate_speed(self, distance, time):
#         traffic = int(input("Please input the traffic cars"))
#         speed = distance/time/traffic
#         print(f"The speed is {speed}")

# class Train(Transport):
#     def __init__(self, name, capacity):
#         super().__init__(name, capacity)
      

#     def calculate_speed(self,distance,time):
#         numberOfStops = int(input("please input the number of stops"))
#         speed1 = distance/time/numberOfStops
#         return f"{self.name} has made {speed1} stops"
    
#     def seat_reservation(self):
#         print(f"{self.name} has reserved a seatnumber")

# tata = Train("tata",30)
# print(tata.calculate_speed(100,20))
  

# Question 38
# class Animal(ABC):
#     def __init__(self,species,age):
#         self.species = species
#         self.age = age
    
#     @abstractmethod
#     def make_sound(self):
#         pass
    
# class Lion(Animal):
#     def __init__(self, species, age):
#         super().__init__(species, age)
    
#     def make_sound(self):
#         return f"The {self.species} roars"
    
#     def feeds(self):
#         print("The {self.species} eats food")
   
# class Elephant(Animal):
#     def __init__(self, species, age):
#         super().__init__(species, age)

#     def make_sound(self):
#         return f"The {self.species} trumpets"
    
#     def display_info(self):
#         print(f" {self.species}\n {self.age}\n {self.make_sound()}")

# Elephant1 = Lion("mammal",34)
# Elephant1.feeds()
    

class Discount(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def apply_discount(self,price):
        pass
    

        
        
    

    
    
    

