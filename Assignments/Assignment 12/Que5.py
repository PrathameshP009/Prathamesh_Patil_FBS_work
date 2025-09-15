#Python Program to Count the Number of Vowels in a String
s = "hello world"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel Count:", count)
