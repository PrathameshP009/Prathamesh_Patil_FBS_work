# Write a program to find maximum and minimum element in a list
list1 = [3, 7, 2, 9, 5]
maximum = list1[0]
minimum = list1[0]
for num in list1:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Max =", maximum)
print("Min =", minimum)
 