str = input()
temp = "0"
sum = 0
for ch in str:
    if(ch.isdigit()):
        temp += ch
    else:
        sum += int(temp)
        temp = "0"
    Sum = sum + int(temp)
print(Sum)