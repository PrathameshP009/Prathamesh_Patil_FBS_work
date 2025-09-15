#Write a program to remove duplicates from the list
list1 = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in list1:
    found = False
    for u in unique:
        if u == num:
            found = True
            break
    if not found:
        unique.append(num)
print("Without duplicates:", unique)
