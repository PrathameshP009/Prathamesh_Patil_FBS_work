# Get the start and end of the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Numbers between {start} and {end} that are divisible by 7 and multiples of 5:")

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")
else:
    print("There are no numbers divisible by 7 and multiples of 5")