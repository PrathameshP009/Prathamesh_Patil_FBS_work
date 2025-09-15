num_student= int(input("Enter number of students: "))
percentages= []

for i in range(num_student):
    total = 0
    print(f"Student {i+1}:")
    for s in range(5):
        marks= float(input(f"Enter marks for subject {s+1}: "))
        total += marks
    percent = (total/500) * 100
    percentages.append(percent)
    print(f" Percentage: {percent:.2f}%")

print("\nPercentages of all students:")
for i in range(num_student):
    print(f"Student {i+1}: {percentages[i]:.2f}%")

avg =sum(percentages) / num_student
print(f"\nAverage Percentage: {avg:.2f}%")