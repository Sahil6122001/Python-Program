base = int(input("Enter the base number "))
exponent = int(input("Enter the exponent number"))

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer",result)