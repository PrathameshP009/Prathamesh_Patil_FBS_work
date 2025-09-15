#Write a program to remove all occurrences of a given element in the list
lst = [1, 2, 3, 2, 4, 2, 1, 3]
x = int(input("Enter number to remove: "))
new_list = []
for num in lst:
    if num != x:
        new_list.append(num)
print("Updated list:", new_list)
