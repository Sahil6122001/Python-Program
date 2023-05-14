n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
m= arr[-1]%2==0
n= arr[-1]
s = m+n
print(s)