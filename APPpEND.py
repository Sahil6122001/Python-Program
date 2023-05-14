import array as arr
a = arr.array('i',[])
b = int(input())
for i in range(b):
    a.append(int(input()))
for i in range(b):
    print(a[i])