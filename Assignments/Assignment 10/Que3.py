# Write a program to find the second largest element in the list.
list1 = [3, 8, 2, 9, 5]
first = second = -999999
for num in list1:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest =", second)
