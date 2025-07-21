n= int(input("Enter number for printing prime numbers: "))
count = 0
num = 2

while count < n:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        count += 1
    num += 1
