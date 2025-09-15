#Python Program to count number of digits and letters in a string.
s = "fbs123"
digits = 0
letters = 0
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("Letters:", letters)
print("Digits:", digits)
