# function to insert into an array
def insert_array(array,item,position):
    # insert a given item into the list
    array.insert(position,item)     
    # returns the array after inserting
    return array
x=int(input("enter item to insert : "))
p=int(input("enter position of insertion : "))
array=[1,2,3,7,6,44]
b=insert_array(array,x,p)
print("the element "+str(x)," inserted : ")
print("now array becomes : "+str(b))
