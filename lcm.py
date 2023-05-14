a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1 = min1+1
#using import function
import math
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c = int(input("Enter the Third Number :"))
print("the lcm of given number is ",end=" ")
print(math.lcm(a,b,c))