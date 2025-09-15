n = int(input("Enter the value :"))
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print("Is Palindrome ?", is_palindrome(121))
