def print_z_pattern(n):
    print('*' * n)
    for i in range(n-2, 0,-1):
        spaces = ' ' * i
        print(spaces + '*')
    print('*' * n)
length = 11
print_z_pattern(length)
