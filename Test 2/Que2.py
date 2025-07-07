num = int(input("Enter a 3-digit number :"))

if 100 <= num <= 999:
    first_digit = num // 100
    second_digit = (num // 10) % 10
    third_digit = num % 10 
    
    if first_digit == 2 * second_digit and first_digit * 2 == third_digit :
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Not a 3-digit number")