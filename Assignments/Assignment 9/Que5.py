n = int(input("Enter number : "))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(n))
