print("Enter marks for 5 subjects out of 100:")

a=float(input("Enter marks of 1st subject"))
b=float(input("Enter marks of 2nd subject"))
c=float(input("Enter marks of 3rd subject"))
d=float(input("Enter marks of 4th subject"))
e=float(input("Enter marks of 5th subject"))

total = a + b + c + d + e
Avg = total / 5

print(f"\nTotal Marks = {total}")
print(f"Average = {Avg:.2f}")

if Avg >= 60:
    print("Grade: First Class")
elif Avg >= 50:
    print("Grade: Second Class")
elif Avg >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")