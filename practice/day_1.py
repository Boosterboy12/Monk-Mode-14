class mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price


apple = mobile("apple", 100000)
samsung = mobile("samsung", 2000000)

print(samsung.price)
print(apple.price)
