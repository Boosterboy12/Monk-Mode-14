# The Smart Inventory Tracker
class product:
    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category


class inventory:
    def __init__(self):
        self.items = []

    def add_products(self, *products):
        for item in products:
            self.items.append(item)

    def calculate_total_value(
        self,
    ):
        total = 0
        for item in self.items:
            total += item.price
        return total


p1 = product("PS5", 150000, "GAMING")
p2 = product("BMW", 15000000, "AUTOMOBILE")
p3 = product("PUMA", 1500, "FASHION")
p4 = product("AULA F75", 150000)

my_shop = inventory()
my_shop.add_products(p1, p2, p3, p4)
total_costing = my_shop.calculate_total_value()
print(f"My Shop's total costing: ₹{total_costing}")
