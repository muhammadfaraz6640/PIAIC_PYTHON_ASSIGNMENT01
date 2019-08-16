k=2
b=1
for i in range(1,10):
    for j in range(1,6):
        if i<=5 and j<=i:
            print(b,end="")
            b+=1
        elif i>5 and j<=6-k:
            print(b,end="")
            b+=1
        else:
            print(" ",end="")
    print("\n")
    k+=2
    b=1

