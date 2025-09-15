#Python Program to Find the Second Largest Number in a List Using Bubble sort
numbers = [10, 20, 4, 45, 99]

n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Second Largest:", numbers[-2])
