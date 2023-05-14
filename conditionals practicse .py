a = int(input("first number"))
b = int(input("second number"))
c = int(input("third number"))
d = int(input("fourth number"))

if (a>b):
  print(str(a) + " is greatest")
    
elif(b>c):

    print("b is greatest")
    print(b)
elif(c>d):
    print("c is greatest")
    print(c)
else:
    print("the last value is greatest i.e")
    print(d)

#Marks student
marks1 = int(input("enter first marks: "))
marks2 = int(input("enter second marks: "))
 
if(marks1+marks2)/2 <40:
    print("fail ho padh lo")
else:
    print("pss")
# username length
str = input("enter the name")
if(len(str))<9:
    print("enter more character ")
else:
    print("more than 9 character")