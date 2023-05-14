n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
x = max(arr)
print(x)
y = -9999
for i in range(0,n):
    if(arr[i]<x and arr[i]>y):
        y = arr[i]
print(y)
