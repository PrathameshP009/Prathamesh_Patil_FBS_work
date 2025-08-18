print("Enter marks out of 100 for 5 subjects:")

subject1 = float(input("Marks for Subject 1: "))
subject2 = float(input("Marks for Subject 2: "))
subject3 = float(input("Marks for Subject 3: "))
subject4 = float(input("Marks for Subject 4: "))
subject5 = float(input("Marks for Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

print("\nTotal Marks =", total_marks, "/ 500")
print("Percentage =", percentage,"%")