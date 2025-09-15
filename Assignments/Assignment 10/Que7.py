#/ Write a program to create a new list from existing list which contains cube of each no of list.
list1 = [1, 2, 3, 4]
cubes = []
for num in list1:
    cubes.append(num * num * num)
print("Cubes:", cubes)
