
a = []
n = int(input("the Size of the array is:"))
for i in range(n):
    a.append(int(input("enter the element ")))
for i in range(0,n-1):
    d = len(a)%2==0
    print("even index ",d)
    break
else:
    print("odd index",a)