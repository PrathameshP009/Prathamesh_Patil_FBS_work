x=1
#row
for i in range (1,6):
    #column
    for j in range(1,i+1):
        if(j %2 ==0):
            print("$", end=" ")
        else:
            print("*", end=" ")
        #x += 1
    print()
    