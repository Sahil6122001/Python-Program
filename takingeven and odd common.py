inarr = []
even = []
odd = []
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
        inarr = even + odd
print(*(inarr),sep=' ')