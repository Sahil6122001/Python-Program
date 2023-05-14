from unicodedata import decimal


t =  int(input())
ans = []
for i in range(t):
    A,B=input().split()
    a = int(A)
    b = int(B)
    temp = a+b
    ans.append(temp)

print(ans)
print(max(ans))
final = (bin(max(ans)))
print(final[2:])