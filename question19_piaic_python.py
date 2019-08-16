text=(input("enter text : "))
pal_chk=""
for a in range(len(text)-1,-1,-1):
    pal_chk=pal_chk+text[a]
if pal_chk==text:
    print("you entered a palindrome text ")
else:
    print("you entered a non-palindrome text ")
