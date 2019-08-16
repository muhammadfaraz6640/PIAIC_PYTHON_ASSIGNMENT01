deci=int(input("enter number in decimal : "))
while deci>1  :
    a=deci%2
    if a==0:
        binary=0
        print(binary)
    elif a!=0:
        binary=1
        print(binary)
    deci=int(deci/2)
