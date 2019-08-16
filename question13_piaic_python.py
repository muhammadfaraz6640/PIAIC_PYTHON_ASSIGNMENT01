height=float(input("enter your height in centimeters : "))
weight=float(input("enter your weight in kilo-grams : "))
h=pow((height/100),2)
bmi=weight/h
print(" your body-mass-index : "+str(bmi))
if bmi>25.0:
    print("you are over weihted...!!")
elif bmi>=18.5 and bmi<=24.9:
    print("you are healthy...!!")