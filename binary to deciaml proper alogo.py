n = int(input())
result = 0
multiplier = 1
while(n>0):
    dig = n%2
    result += dig * multiplier
    multiplier *= 10
    n//=2
print(result)