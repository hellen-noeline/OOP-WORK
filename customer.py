class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def displayInfo(self):
        return f'Customer Name: {self.name}\nCustomer Address: {self.address}'


# Creating a customer named Hellen
hellen = Customer("Hellen", "123 Kiwempe Lane, Kampala")

# Displaying Hellen's's information
print(hellen.displayInfo())