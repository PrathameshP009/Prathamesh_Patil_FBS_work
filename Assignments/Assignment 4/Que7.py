n = int(input("Enter a number: "))
i = 1

print("Numbers up to", n, "that are not divisible by 2 and 3:")
while i <= n:
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
    i += 1
