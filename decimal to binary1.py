n = int(input())
a = []
while(n>0):
    dig = n%2
    a.append(dig)
    n = n//2
a.reverse()
for i in a:
    print(i,end ="")