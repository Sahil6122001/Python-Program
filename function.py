#greeting message using functions
def greet(name):
    print("good day, "+name)
greet("sahil")

# adding two number using function
def mysum(num1,num2):
    return(num1+num2)
s =mysum(4,89) 
print(s)
# deafult argument example
def greet(name= "stranger"):
    print("good day, "+name)
greet()