def palindrome(n):
   temp = n
   rev = 0
   while(n>0):
      dig = n%10
      rev = rev*10+dig
      n//=10
      if(temp == rev):
        return True
        break
   else:
      return False
  
n = int(input())
print(palindrome(n))