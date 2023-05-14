#create a list using[]
a = [1,2,3,46,7]
# print the list using print()fn
print(a)

#Acess using index using a[0],a[1]
print(a[2])

#change the value of list
a[0] = 45
print (a) 
# We can create a list with items of different types
b = [45,"Sahil",False,6,9]
print(b)
# List Slicing
Friends = ["Sam","ram",45]
print(Friends[0:1 ])
#List Methods 
li = [1,8,7,2,21,15]
li.sort()#Arrange in Ascending order
print(li)
li.reverse()#Reverse
print(li)
li.append(8)#updates at last
print(li)
li.insert(3,9)#this will add 8 at index 3
print(li)
li.pop(2)#deletes at indes 2
print(li)
li.remove(21)#Replace 21 at list
print(li)
