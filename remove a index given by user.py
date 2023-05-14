n = "121"
digit = "1"
ans=[]
for p in range(len(n)):
    if n[p]==digit:
        temp = n[0:p]+n[(p+1):]
        ans.append(int(temp))
print(str(max(ans)))