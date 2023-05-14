n = int(input())

for i in range(1, (n*2)):
    if i <= n:
        print(" "*(n-i) + "*"*(i))
    else:
        print(" "*(i-n) + "*"*(2*n-i))