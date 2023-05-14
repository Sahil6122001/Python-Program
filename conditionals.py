a = 100
if (a>46):
    print("a is greater than 46 ")
if(a>36):
    print("a is greater than 36")
if(a<45):
    print("a is smallest than 45")
else:
    print("a is greater than 45")
    print(a)

# write a program to print yes if age entered is 18 or greater than 

a = int(input("enter the age"))
if (a > 18):
    print("yes")
elif (a == 18):
    print("yes")
else:
    print("sorry")
 
# and operator

b = int(input("enter the age"))
if (b<18 and b>46):
    print("ys you can")
else:
    print("sorry")

# or operator
c = int(input("enter the age"))
if (c<18 or c>46):
    print("ys you can")
# is statement
c = None
if(c is None):
    print("yes")
else:
    print("no")
# in student
d = [2,45,6]
if(56 in d):
       print("true")









