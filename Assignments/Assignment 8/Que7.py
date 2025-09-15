n=int(input("Enter a number: "))
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print("Sum of digits:", sum_of_digits(n))
