k=2
for i in range(1,10):
    for j in range(1,6):
        if i<=5 and j<=i:
            print("*",end="")
        elif i>5 and j<=6-k:
            print("*",end="")            
        else:
            print(" ",end="")
    print("\n")
    k+=2
