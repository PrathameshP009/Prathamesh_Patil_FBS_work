# Write a program to create a duplicate of an existing list. It should not point to same memory location.
lst = [1, 2, 3, 4]
copy = []
for num in lst:
    copy.append(num)
print("Original:", lst)
print("Copy:", copy)
