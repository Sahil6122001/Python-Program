#mutiplication table



num = int(input("enter the number whose multiplication tou want to show : "))
for i in range(1,11):
      print(num, 'X',i,'=', num*i)
#Printing greeting for each user in list
users = ['Sahil','Saurav','Ram']
for i in users:
   #print("Hello    " +i)
   # prime or not
 num =  int(input("enter a number to check whether it is prime or not: "))
for i in range (2,num):
    if (num%i ==0):
            print("the number is not prime")
            break
else:
          print("the number is prime")

# factorial of the given number
num = int(input("Enter the number: "))
factorial = num*(num-1)
print(f"The factorial of {num} is {factorial}")
# Sum of first n natural number
num = int(input("enter an integer"))
while(num>0):
     natural = num*(num+1)/2
     print("the sum of natural number are"+str(natural))
     break
 # pattern printing  without space
n = 3
for i in range(3):
     print("*"*i)
# pattern printng with space
n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
# printing table in reverse order
num = int(input("enter the number whose multiplication tou want to show : "))
for i in range(1,11):
     print(num*i)
