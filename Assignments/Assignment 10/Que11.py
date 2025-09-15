#Write a program to print all numbers which are divisible by m and n in the list.
lst = [10, 12, 15, 18, 20, 24, 30]
m = 3
n = 5
for num in lst:
    if num % m == 0 and num % n == 0:
        print(num)
