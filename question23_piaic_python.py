b=1
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(b,end="")                   
        else:
            print(" ",end="")
    print("\n",end="")
    b+=1

