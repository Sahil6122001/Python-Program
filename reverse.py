num  = int(input("enter the number to be reversed:"))
rev = 0
while(num>-0):
    dig = num%10
    rev = rev*10+dig
    num = num//10
print("the reversed number is ",rev)