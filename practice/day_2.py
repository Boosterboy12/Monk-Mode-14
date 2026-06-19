# Create a Python class called Coffee that displays a menu of drinks and allows the user to place an order. The program should:
# Show at least three drink options.
# Take the user's order as input.
# Accept inputs regardless of letter case.
# Display a confirmation message for valid orders.
# Display an error message for invalid orders.
# Thank the customer before the program ends.

# --- Solution --- #
class Cofee:
    def order(self):
        print("1 = Chai - $20, 2 = Cold Coffee - $30, 3 = Hot Cofee - $30")
        a = input("Select Your Order : ",).lower()
        if a == "chai":
            print("Thanks ! Your Chai Is Ready")

        elif a == "cold coffee":
            print("Thanks ! Your Cold Cofee Is Ready")

        elif a == "hot coffee":
            print("Thanks ! Your Hot Cofee Is Ready")

        else:
            print("Please Enter A Valid Demand Other Wise Chatty And Sparky Will Beat You")

        print("Thankyou For Your Convinience !")

shop = Cofee()
shop.order()


