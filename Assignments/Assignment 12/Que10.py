#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
s1 = "Hello"
s2 = "Fbs"
length1 = 0
length2 = 0

for _ in s1:
    length1 += 1
for _ in s2:
    length2 += 1

if length1 > length2:
    print("Larger String:", s1)
else:
    print("Larger String:", s2)
