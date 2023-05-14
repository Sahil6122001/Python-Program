greeting = "Good Morning ,"
name =  "sahil saurav"
#Concatenating two String 
print(greeting + name)
#Printing First Index of name
print(name[0:3])
#Slicing
print(name[2:-1])
#Skiping
print(name[0:1:2])
#string Function(length),endswith,capitalize,count,find,replace
print(len(name)) 
print(name.endswith("l"))
print(name.capitalize())
print(name.count("a"))
print(name.find("S"))
print(name.replace("sahil","Ss"))
#escape sequences
name = "Sahil\nsaurav"
a = "Sahil\tsaurav"
b = "Sahil\'Saurav"
c = "Sahil\\saurav"
print(name,a,b,c)