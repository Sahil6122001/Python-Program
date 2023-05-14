n = input()
a= n[::-1]
if(a==n):
    print("palindrome")
else:
    print("not palindrome")

# using function

def reverse(n):
    a = n[::-1]
    if(a==n):
        print('palindrome')
    else:
        print('not palindrome')
n = input()
print(reverse(n))