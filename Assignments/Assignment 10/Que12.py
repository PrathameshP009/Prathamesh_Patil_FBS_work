# Write a program to create three lists of numbers, their squares and cubes using list comprehension.
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)