total = 0
n =int(input("Enter no. of employees: "))
emp = 1

while emp <= n:
    b =float(input("Enter basic salary: "))
    if b < 20000:
        da = b * 0.10
        ta = b * 0.12
        hra = b * 0.15
    else:
        da = b * 0.15
        ta = b * 0.18
        hra = b * 0.20

    sal = b + da + ta + hra
    print("Total salary:", sal)
    total = total + sal
    emp += 1
print("Total salary of all employees:", total)
