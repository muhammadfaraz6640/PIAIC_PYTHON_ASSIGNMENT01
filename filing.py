# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:29:48 2019

@author: Haroon Traders
"""
# filing 
# read "r"
#append "a"
#with open('textfile.txt','w')as file:
#  print(file.writable())
 #   file.write("name")
'''
with open('textfile.txt','w')as file:
    file.writelines("faraz ansar")
with open('textfile.txt','r')as file:
    print(file.read())
with open('textfile.txt','w')as file:
    file.writelines("\n kaala")
with open('textfile.txt','w') as file:
    file.write("khaalio")
with open('textfile.txt','r')as file:
    element=file.read()[0]
    file.close()
print(element)
var= open('textfile.txt','r')
print(var.read())   # append mode for avoid overwriting

# modules: use of finctions from other files in another files called modules and key word is import
def add(a,b):
    return a+b
import filing as shortname

a=shortname.add(2,3)
print(a)
file=open("revfile.txt","w")
file.write("hello world")
file.close() 
dict={'dado':'hello','mazo':'faraz'}
a=str(input("enter into alien language"))
for k in dict.keys():
    if a==k:
        print(dict[k])
'''
dict={'key1':{'key2':'faraz','key3':'umer'}}
print(dict['key1']['key2'])