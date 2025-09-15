#Python Program to Sort the List According to the Second Element in Sublist
list1 = [[1, 3], [2, 1], [4, 2]]
sorted_list = sorted(list1, key=lambda x: x[1])
print("Sorted List:", sorted_list)
