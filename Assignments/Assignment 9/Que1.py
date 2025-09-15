n = int(input("Enter number : "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sum_of_factorials(n):
    if n == 0:
        return 0
    return factorial(n) + sum_of_factorials(n - 1)
print("Sum of factorials:", sum_of_factorials(n))
