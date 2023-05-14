

n=int(input())
l=[int(x) for x in input().split()]
l=list(set(l))
l.sort()
if(len(l)<2):
    print(-1)
else:
    print(l[len(l)-2])
