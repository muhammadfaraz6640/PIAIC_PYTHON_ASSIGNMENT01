text=str(input("enter text : "))
vowel=int(0)
consonant=int(0)
for a in range(0,len(text)):
    if text[a]=='a' or text[a]=='e' or text[a]=='i' or text[a]=='o' or text[a]=='u' or text[a]=='A' or text[a]=='E' or text[a]=='I' or text[a]=='O' or text[a]=='U':
        vowel+=1
    else:
        consonant+=1
print("vowels : "+str(vowel))
print("consonant : "+str(consonant))
