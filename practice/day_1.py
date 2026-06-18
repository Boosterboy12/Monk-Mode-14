# Q1: Design a Mobile class to represent different smartphone models with their company name and price.
# --- Solution --- #
class Mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price


apple = Mobile("apple", 100000)
samsung = Mobile("samsung", 2000000)

print(samsung.price)
print(apple.price)


# Q2: Design a Player class for a cricket team where all players belong to the same team but have different names.
# --- Solution --- #
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
# --- Solution --- #
class Laptop:
    def __init__(self, company, ram):
        self.company = company
        self.ram = ram


laptop_1 = Laptop("Victus", 16)
laptop_2 = Laptop("Victus", 16)

print(
    laptop_1
    == laptop_2  # Prints False as both the objects have different memory location
)

# Practice Problem: Write a function called demo() that accepts two parameters: a name and an age. The function should print these values directly to the console.
# Given Input:
# name = "Kelly"
# age = 25


# --- Solution --- #
def demo(name, age):
    print("Name = ", name, "\n" "Age = ", age)


demo(name="Kelly", age=25)

# Practice Problem: Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.
# Given Input:
# Call 1: func1(20, 40, 60)
# Call 2: func1(80, 100)


# --- Solution --- #
def func1(*number):
    for i in number:
        print(i)


func1(10, 20, 30, 40, 50, 60)

# Practice Problem: Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.
# Given Input:
# a = 40
# b = 10


# --- Solution --- #
def calculation(number_1, number_2):
    return number_1 + number_2, number_1 - number_2


a = calculation(40, 10)
print(a)

# Practice Problem: Create a function show_employee() that accepts an employee’s name and salary. If the salary is not provided in the function call, the function should automatically assign a default value of 9000.
# Given Input:
# Case 1: name="Ben", salary=12000
# Case 2: name="Jessa" (salary missing)


# --- Solution --- #
def show_employee(name, salary=9000):
    print("Name : ", name, "\nSalary : ", salary)


show_employee(name="Ben", salary=13000)
show_employee(name="Jessa")
