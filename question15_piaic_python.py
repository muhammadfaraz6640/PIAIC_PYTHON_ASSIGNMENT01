num=int(input("enter atleat 4 digit number"))
sum=0
while num>0:
    x=int(num%10)
    sum=sum+x
    num=num/10
print("sum : "+str(sum))