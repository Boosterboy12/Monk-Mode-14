class Cofee:
    def order(self):
        print("1 = Chai - $20, 2 = Cold Coffee - $30, 3 = Hot Cofee - $30")
        a = input("Select Your Order : ")
        if a == "Chai":
            print("Thanks ! Your Chai Is Ready")

        elif a == "Cold Coffee":
            print("Thanks ! Your Cold Cofee Is Ready")

        elif a == "Hot Coffee":
            print("Thanks ! Your Hot Cofee Is Ready")

        else:
            print("Please Enter A Valid Demand Other Wise Chatty And Sparky Will Beat You")

        print("Thankyou For Your Convinience !")

shop = Cofee()
shop.order()
