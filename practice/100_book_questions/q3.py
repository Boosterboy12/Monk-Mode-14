# Temperature Converter
class temperature_converter:
    def __init__(self):
        pass

    def celcius_to_fahrenheit(self):
        celcius_input = int(input("Enter The Degree Celcius Value : "))
        convert_to_fahrenheit = (celcius_input * 9/5) + 32 
        print(f"The Fahrenheit Value OF {celcius_input} is {convert_to_fahrenheit}")

    def fahrenheit_to_celcius(self):
        fahrenheit_input = int(input("Enter The Degree Fahrenheit Value : "))
        convert_to_celcius = (fahrenheit_input - 32) * 5/9
        print(f"The Celcius Value OF {fahrenheit_input} is {convert_to_celcius}")

    def celcius_to_kelvin(self):
        celcius_input = int(input("Enter The Degree Celcius Value : "))
        convert_to_kelvin = celcius_input + 273.15
        print(f"The Kelvin Value OF {celcius_input} is {convert_to_kelvin}")

    def kelvin_to_celcius(self):
        kelvin_input = int(input("Enter The Degree Kelvin Value : "))
        convert_to_celcius = kelvin_input - 273.15 
        print(f"The Celcius Value OF {kelvin_input} is {convert_to_celcius}")

    def fahrenheit_to_kelvin(self):
        fahrenheit_input = int(input("Enter The Degree Fahrenheit Value : "))
        convert_to_kelvin = (fahrenheit_input - 32) * 5/9 + 273.15
        print(f"The Kelvin Value OF {fahrenheit_input} is {convert_to_kelvin}")

    def kelvin_to_fahrenheit(self):
        kelvin_input = int(input("Enter The Degree Kelvin Value : "))
        convert_to_fahrenheit = (kelvin_input - 273.15) * 9/5 + 32
        print(f"The Fahrenheit Value OF {kelvin_input} is {convert_to_fahrenheit}")


converter = temperature_converter()
converter.celcius_to_fahrenheit()
