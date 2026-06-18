# Q1: Design a Mobile class to represent different smartphone models with their company name and price.
class Mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price


apple = Mobile("apple", 100000)
samsung = Mobile("samsung", 2000000)

print(samsung.price)
print(apple.price)


# Q2: Design a Player class for a cricket team where all players belong to the same team but have different names.
class Player:
    team = "CHENNAI SUPER KINGS"

    def __init__(self, name):
        self.name = name


player_1 = Player("Vihaan")
player_2 = Player("Rahul")
player_3 = Player("Sameer")
print(player_1.name)
print(player_2.name)
print(player_3.name)

# # Q3: Design a Laptop class to verify if two objects with identical specifications share the same memory location or occupy distinct spaces.
class Laptop:
    def __init__(self, company, ram):
        self.company = company 
        self.ram = ram 

laptop_1 = Laptop("Victus", 16)
laptop_2 = Laptop("Victus", 16)

print(laptop_1 == laptop_2) # Prints False as both the objects have different memory location