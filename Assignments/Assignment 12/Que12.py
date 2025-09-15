#Python Program to count number of lowercase characters in a string.
s = "Hello Fbs"
count = 0
for char in s:
    if char.islower():
        count += 1
print("Lowercase letters:", count)
