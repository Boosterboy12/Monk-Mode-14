class identity:
    def __init__(self):
        pass

    def greet(name, age, profession):
        name = input("Enter You Name : ")
        age = int(input("Enter Your Age : "))
        profession = input("Enter The Profession You Love FROM THE FOLLOWING : 1.Coder, 2. Developer, 3. Tech Enthusiast - ")
        print(f"Welcome {name} as you are a {profession} we would like you to answer the follwoing questions")

vihaan = identity.greet("Vihaan", 13, "Coder" )
