#Python Program to Put Even and Odd elements of a List into two Different lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers :", even)
print("Odd numbers :", odd)
