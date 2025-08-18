start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {stop} are:")

for i in range(start, stop+ 1):
    num_str = str(i)
    power = len(num_str)

    total = sum(int(digit) ** power for digit in num_str)
    
    if i== total:
        print(i, end=" ")
