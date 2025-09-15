#Write a program to print list after removing even numbers.
nums = [1, 2, 3, 4, 5, 6, 7]
odd_nums = [n for n in nums if n % 2 != 0]
print("After removing even numbers:", odd_nums)
