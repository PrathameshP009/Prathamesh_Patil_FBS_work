start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the number to check divisibility: "))

print(f"Numbers between {start} and {end} divisible by {divisor}:")

for num in range(start, end + 1):
    if num % divisor == 0:
        print(num, end=" ")
