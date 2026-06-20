# Given a non-negative integer $n$, write a recursive function to calculate the sum of its digits. You must solve this problem without utilizing any iterative loops (for or while).
def sum_int(n):
    if n == 0:
        return 0
    return n % 10 + sum_int(n // 10)
sum = sum_int(454)
print(sum)

# Given a non-negative integer $n$, write a recursive function to determine the total count of digits present in the number. The solution must be implemented implicitly or explicitly without any loops (for or while) or type casting functions (e.g., converting the integer to a string using str(n) is strictly prohibited).
def count_digits(n):
    n

count_digits(32)