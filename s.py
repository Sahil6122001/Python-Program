n = int(input())
total = 0
for i in range(1,n+1):
    if not (i%2 == 0):
        total = i+total
print(total)