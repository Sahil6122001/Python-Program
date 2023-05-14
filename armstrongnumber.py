num = int(input("enter the number :- "))
temp = num
sum = 0
while(temp>0):
    dig = temp%10
    sum += dig**3
    temp//=10
if(num == sum):
    print("the number is armstrong",num)
else:
    print("the number is not armstrong",num)

def armstrong(n):
    temp = n
    sum = 0
    while(temp>0):
        dig = temp%10
        sum += dig**3
        temp //=10
    if(n==sum):
        return True
    else:
        return False
n = int(input())
print(armstrong(n))