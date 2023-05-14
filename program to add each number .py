n = int(input())
sum = 0
while(n!=0):
    dig = int(n%10)
    sum+= dig
    n = n/10
print(sum)