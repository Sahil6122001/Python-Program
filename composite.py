n = int(input())
if(n<4):
    print("not composite")
for i in range(2,n):
    if(n%i==0):
        print("composte")
        break
    else:
        print("not como")
        break