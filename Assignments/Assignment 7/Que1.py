#row
for i in range (1,6):
    for j in range(1,7-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        if(j==1 or i==j):
            print(" * ",end=" ")
        else:
            
            print("   ",end=" ")
    print()
#decreasing triangle
for i in range (1,5):
    for j in range(1,i+1):
        print(" ", end=" ")
    for j in range (1,6):
        if(j==1 or j==5-i):
            print("  * ",end=" ")
        else:
            print("   ",end=" ")
    print()
    