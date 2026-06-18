# Q1: Design a Mobile class to represent different smartphone models with their company name and price.
class mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price


apple = mobile("apple", 100000)
samsung = mobile("samsung", 2000000)

print(samsung.price)
print(apple.price)


# Q2: Design a Player class for a cricket team where all players belong to the same team but have different names.
class players:
    team = "CHENNAI SUPER KINGS"

    def __init__(self, name):
        self.name = name


player_1 = players("Vihaan")
player_2 = players("Rahul")
player_3 = players("Sameer")
print(player_1.name)
print(player_2.name)
print(player_3.name)

# # Q3: Design a Laptop class to verify if two objects with identical specifications share the same memory location or occupy distinct spaces.
class laptop:
    def 