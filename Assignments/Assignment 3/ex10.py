gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

# Check eligibility
if gender == "male":
    if age >= 21:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
elif gender == "female":
    if age >= 18:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
else:
    print("Invalid gender entered.")