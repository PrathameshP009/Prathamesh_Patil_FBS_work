# Write a program to reverse the list
list = [1, 2, 3, 4, 5]
rev = []
for i in range(len(list)-1, -1, -1):
    rev.append(list[i])
print("Reversed List:", rev)
