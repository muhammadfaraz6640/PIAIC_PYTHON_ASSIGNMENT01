import math
x1=int(input("enter co-ordinate for x1 : "))
x2=int(input("enter co-ordinate for x2 : "))
y1=int(input("enter co-ordinate for y1 : "))
y2=int(input("enter co-ordinate for y2 : "))
x=pow((x2-x1),2)
y=pow((y2-y1),2)
distance=math.sqrt((x+y))
print("The distance between the points ("+str(x1),","+str(x2),") and ("+str(y1),","+str(y2),") is : "+str(distance))

