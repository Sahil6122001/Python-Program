n = int(input())
total = 0
while(n>0):
    dig = n%10
    total = total+dig
    n = n//10
print(total)
if(total%2==0):
    print("even")
else:
    print("odd")