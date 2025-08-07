# Write a program to find factorial of all no. in given range using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_in_range(start, end):
    if start > end:
        print("Invalid range. Start should be less than end")
        return

    for num in range(start, end + 1):
        print(f"Factorial of {num} is {factorial(num)}")

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))
factorial_in_range(start_range, end_range)
