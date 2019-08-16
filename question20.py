text=str(input("enter text : "))
digits=0
alphabets=0
spe_chr=0
for a in range(0,len(text),1):
    b=ord(text[a])
    if (b>=65 and b<=90) or (b>=97 and b<=122) :
        alphabets+=1
    elif b>=48 and b<=57 :
        digits+=1
    else:
        spe_chr+=1
    b=''
print("digits : "+str(digits))
print("alphabets : "+str(alphabets))
print("special characters : "+str(spe_chr))