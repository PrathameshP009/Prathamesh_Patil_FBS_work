number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

sum_of_digits = hundreds + tens + units

print("Sum of digits:",sum_of_digits)