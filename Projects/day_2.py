class emplyee:

    def __init__(self, name, age, salary=1000):
        self.name = name 
        self.salary = salary
        self.age = age

    def hire( name, age):
        try:
            attendee_name = input("Enter Your Name - ").lower()
            attendee_age = int(input("Enter Your Age - "))

            if name == int:
                print("Please Enter A Valid String Name")

        except:
            print("Please Enter A Valid Input !")

        else:
            print(f"Well Done {name} You Have Been Selected For The Job")
        finally:
            print("Glad You Choose To Invest Your Precious Time With Us !")

new_emplyee = emplyee.hire("Vihaan", 12)
