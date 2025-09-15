#Write a program to print list after removing even numbers.
list = [1, 2, 3, 4, 5, 6]
result = []
for num in list:
    if num % 2 != 0:
        result.append(num)
print("After removing even numbers:", result)
