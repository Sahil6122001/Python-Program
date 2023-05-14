a = []
b = []
n = int(input())
a = list(map(int,input().strip().split(',')))[:n]
b = list(map(int,input().strip().split(',')))[:n]
if(sorted(a) == sorted(b)):
    print(1)
else:
    print(0)