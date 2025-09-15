# Accept a number from user and check if this element is present in the list or not.
list1 = [1, 2, 3, 4, 5]
n = int(input("Enter a number to search: "))
count = 0
for num in list1:
    if num == n:
        count += 1
if count > 0:
    print(n, "is present", count, "times.")
else:
    print(n, "is not present.")
