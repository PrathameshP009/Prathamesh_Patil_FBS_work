# a. 1! + 2! + 3! + ... + n!
n = int(input("Enter n for factorial sum: "))
fact_sum = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    fact_sum += fact
print("Sum of factorials:", fact_sum)

# b. N + N^2 + N^3 + ... + N^N
N = int(input("\nEnter N for power sum: "))
power_sum = 0
for i in range(1, N+1):
    power_sum += N ** i
print("Sum of powers:", power_sum)

# c. Geometric series sum from 1 to n, common ratio 2
n = int(input("\nEnter n for geometric series: "))
geo_sum = 0
for i in range(n):
    geo_sum += 2 ** i
print("Geometric series sum:", geo_sum)

# d. S = a + a^2/2 + a^3/3 + ... + a^10/10
a = int(input("\nEnter a for special series: "))
special_sum = 0
for i in range(1, 11):
    special_sum += (a ** i) / i
print("Special series sum:", special_sum)

# e. x - x^2/3 + x^3/5 - x^4/7 + ... to n terms
x = int(input("\nEnter x for alternating series: "))
n = int(input("Enter number of terms: "))
alt_sum = 0
sign = 1
den = 1
for i in range(1, n+1):
    alt_sum += sign * (x ** i) / den
    sign *= -1
    den += 2
print("Alternating series sum:", alt_sum)