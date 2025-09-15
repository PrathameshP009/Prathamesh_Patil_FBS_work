#Write a program of having n number of elements in the list and find out even and old numbers in the list.
lst = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even List:", even)
print("Odd List:", odd)
