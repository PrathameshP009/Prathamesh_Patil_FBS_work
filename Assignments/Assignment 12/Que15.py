#Python Program to find larger string without using built-in functions.
s1 = "elephant"
s2 = "dog"
len1 = 0
len2 = 0

for _ in s1:
    len1 += 1
for _ in s2:
    len2 += 1

if len1 > len2:
    print("Larger String:", s1)
else:
    print("Larger String:", s2)
