"""
The Smart Inventory Tracker (Enterprise Edition)
Author: Vihaan
Description: A robust inventory management system with automated cost validation.
"""

# Defining product values & conditions for ft
class product:
    def __init__(self, name, price, category="General"):
        if price >= 20000000:
            print(
                "Error 1012: Invalid Cost, Please Enter A Valid Cost"
            )  # Prints the text but doesn't throw an error
            self.is_valid = False  # This is to ensure that the code doesn't add this invalid cost in the final cost
            return

        # Defining the values
        self.name = name
        self.price = price
        self.category = category
        self.is_valid = True

        print(name) # Printing the details
        print(price)
        print(category)

# Adding itmes and calculations to the inventory
class inventory:
    def __init__(self):
        self.items = [] # Makes a blank list we'll fill this later

    def add_products(self, *products): # To add itmes to your shop 
        for item in products:
            if item.is_valid:
                self.items.append(item)

    def calculate_total_value(
        self,
    ):
        total = 0 # Making the total cost 0 so the cost starts from 0 
        for item in self.items:
            total += item.price # Adding each item's price here 
        return total


p1 = product("PS5", 150000, "GAMING") # Adding the products
p2 = product("BMW", 105000000, "AUTOMOBILE")
p3 = product("PUMA", 1500, "FASHION")
p4 = product("AULA F75", 150000)

my_shop = inventory() # Creating our shop
my_shop.add_products(p1, p2, p3, p4) # Adding items to our shop
total_costing = my_shop.calculate_total_value() # Finding the total costing of the items in our shop
print(f"Your empire holds" f" ₹{total_costing}" " worth of digital power ⚡") # Finally printing the total cost of our shop's products
