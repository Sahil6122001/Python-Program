myDict = {
    "Fan" : "Pankha",
  "Clock" : "Ghadi",
  "Laptop" : "Me"
}
print("Option are",myDict.keys())
a = input("Enter the English word\n")
print("The Meaning of your word:",myDict.get(a))
# 2 Unique Number From User
a = int(input("Enter the First Number:\n"))
b = int(input("Enetr the second Number:\n"))
c =int(input("Enter the Third Number:\n"))
d = int(input("Enter the Fourth Number:\n"))
s = {a,b,c,d}
print(s)
# language Problem
myDict1 ={
    
}
a =input("Enter the language of Sahil\n")
b = input("enter the LAnguage of Saurav\n")
c = input("enter the Language of Sahil\n")
d = input ("eNTER the language of shyam\n")
myDict1 ['Sahil']= a
myDict1 ['Saurav']= b
myDict1 ['Sahil']= c
myDict1 ['shyam']= d
print(myDict1)