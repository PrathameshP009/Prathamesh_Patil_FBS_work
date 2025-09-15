#Python Program to Detect if Two Strings are Anagrams.
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
