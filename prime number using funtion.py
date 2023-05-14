def prime():
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                return False
            else:
                return True
n = int(input())
print(prime())
