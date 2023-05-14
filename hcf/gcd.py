import math
a = int(input("enter the first number:-"))
b = int (input("enter the second number:-"))
c = int (input("enter the third number:-"))
print("the gcd/hcf of 3 numbers is :- " ,end="")
print(math.gcd(a,b,c))
#without using math function
x= int(input("enter the number"))
y = int(input("enter the 2 number"))
if x > y:
        smaller = y
else:
        smaller = x
for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 


print("The H.C.F. is", i)