bin=int(input("enter the binary number : "))
n=int(input("enter number of binary digits : "))
res=0
for a in range(0,n,1):
    b=bin%10
    dec=int(pow((b*2),a))
    print(dec)
    res=int(res+dec)
    bin=bin/10
print("decimal : "+str(res))
