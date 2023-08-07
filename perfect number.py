n = int(input())
s = 0
for i in range(1,n):
    if (n%i == 0):
        s = s+i
if(s == n):
    print("perfect number",n)
else:
    print("dusra daal")

#second attempt
n = int(input("enter the number:- "))
s = 0
for i in range(1,n):
    if(n%i==0):
        s = s+i
if(s==n):
    print(f"{n} is a perfect number ")
else:
    print(f"{n} the number you enterd is not a perfect no")