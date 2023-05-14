#Sets
a = {1,2,3,4,1}#Sets deletes the Duplicate elements
print(type(a))
print(a)
#Declaring an empty Set 
b ={}
b = set()
print(type(b))
b.add(3)
b.add(3)#Sets is a collection of non repetitive element
b.add(6)
b.add((4,5,7))# we can tuple in sets 
print(len(b))# Prints the Length of the set
b.remove(3)# Removes 3 from set
print(b.pop())