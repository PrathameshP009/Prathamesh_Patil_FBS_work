char = input("Enter a single alphabet: ")
if len(char) == 1 and char.isalpha():
    char = char.lower()
    if char in ('a', 'e', 'i', 'o', 'u'):
        print("The alphabet is a vowel.")
    else:
        print("The alphabet is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet.")
