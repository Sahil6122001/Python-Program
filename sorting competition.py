a = []
n = int(input())
temp = 0
for i in range(n):
    a.append(int(input()))
for element in a:
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[i])>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
for i in range(0,len(a)):
    print(a[i])