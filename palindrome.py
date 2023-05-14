num = int(input("enter the number to check whether it is palindrome or not :- "))
temp = num
rev = 0
while(num>0):
    dig  =num%10
    rev = rev*10 + dig
    num = num//10
if(temp == rev):
 print("the number is palindrome",temp)
else:
    print("the numbere is not palindrome",temp)

# Using Functions
def palindrome(n):
   temp = n
   rev = 0
   while(n>0):
      dig = n%10
      rev = rev*10+dig
      n//=10
      if(temp == rev):
         return True
      else:
         return False
n = int(input())
print(palindrome(n))