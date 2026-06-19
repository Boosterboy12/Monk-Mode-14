class emplyee:

    def __init__(self, name, age, salary=1000):
        self.name = name 
        self.salary = salary
        self.age = age

    def hire(name, age):
        try:
            attendee_name = str(input("Enter Your Name - ")).lower()
            attendee_age = int(input("Enter Your Age - "))

        except:
            print("Please Enter A Valid Input !")
        
        finally:
            print("Glad You Choose To Invest Your Precious Time With Us !")

new_emplyee = emplyee.hire("Vihaan", "shs")
