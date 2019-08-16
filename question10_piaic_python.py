principal=int(input("enter principal amount : "))
interest=float(input("enter interest in % : "))
time=int(input("enter duration in years : "))
inter_in_deci=interest/100
result=principal*(1+(inter_in_deci*time))
print("after "+str(time)," years , your principal amount "+str(principal)," over an interest of "+str(interest)," is about : "+str(result)," rupees ")

