def print_factors(number):
    if number <= 0:
        print("Please enter a positive integer.")
        return

    print(f"Factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
num = int(input("Enter a positive integer: "))
print_factors(num)
