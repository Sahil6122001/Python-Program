def number(n):
    if(n>26):
        p = [int(i) for i in str(n)]
        return number(sum(p))
    else:
        return n

a = input()
p = [int(i) for i in a]
s = sum(p)
s1 = number(s)
print(chr(s1+64))
# Second Method without using function
a = input()
p = [int(i) for i in a]
s = sum(p)
if(s>26):
   s1 =  [int(i) for i in str(s)]
   s2 = sum(s1)
   print(chr(s2+64))
else:
    print(chr(s+64))
