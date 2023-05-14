def greatest(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
         return num2
        else:
            return num3

num1 = int(input("enter the number:  "))
num2 = int(input("enter the number:  "))
num3 = int(input("enter the number:  "))       
        

s = greatest(num1,num2,num3)
print("the greatest number is "+str(s))

# celsius to fahrenheit

def fahrenheit(i):
    return   (i * (9/5)) + 32 
i = int(input("enter the number:  "))
s = fahrenheit(i)
print("the value in f is :"  +str(s))

# recursive function while printing sum of n natural numbers
def recursive(i):
    if i ==0:
        return 1
    else:
        return i*(i+1)/2
i = int(input("enter the number:  "))
s = recursive(i)
print("the value is :" +str(s))

# strip a word
def remove_split():
 email = input("enter here : ")
 print(email.split('@')[0])
