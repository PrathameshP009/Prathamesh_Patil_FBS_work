#Python Program to Remove the nth Index Character from a Non-Empty string
s = "FirstBit"
n = int(input("Enter the index of character to remove: "))
new_s = s[:n] + s[n+1:]
print(new_s)
