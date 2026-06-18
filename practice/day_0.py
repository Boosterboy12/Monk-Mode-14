# Task-1: Create a function that takes a number as a input and prints The even number between 1 and the given number.
#  --- Solution --- #
 
def count_even(n):
    count = 0
    for i in range(1, n+1 ):
        if i %2 == 0:
            print(i)
            count += 1
    return count 
result = count_even(20)
print(result)

# Task-2: Create a function that tells that whether a student is pass or fail by taking the marks as the input telling the student is pass or fail. 
# --- Solution --- #

marks = int(input("Enter Your Marks : "))
def check_result(marks):
    if marks >= 40:
        print("Pass")

        if marks >= 90: # Add On: If student's marks are greater & equal to 90 displays "Distinction"
            print("Distinction")
    else:
        failed_by = 40 - marks
        print(f"Failed By {failed_by} Marks")
output = check_result(marks)


class vihaan:
    def __init__(self):
        pass
    def greet(name):
        name= "Vihaan"
        return("Hello", name)
    