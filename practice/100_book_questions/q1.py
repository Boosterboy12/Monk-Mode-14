# A basic calculator
try:
    number_1 = int(input("Enter Your Desired Number_1: "))
    number_2 = int(input("Enter Your Desired Number_2: "))

except:
    raise Warning("WRONG INPUT")


else:

    def add(number_1, number_2):
        return number_1 + number_2

    def subtract(number_1, number_2):
        return number_1 - number_2

    def multiply(number_1, number_2):
        return number_1 * number_2

    def divide(number_1, number_2):
        if number_2 != 0:
            return number_1 / number_2
        else:
            print("Division By Zero")

    def modulus(number_1, number_2):
        return number_1 % number_2

    def exponential(number_1, number_2):
        return number_1**number_2


result = add(number_1, number_2)
print(result)
