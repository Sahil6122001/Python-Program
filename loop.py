#printng i 50 times



i = 0
while(i<=50):
    print(str(i)+ "  Value of i ")
    i=i+1
else:
    print("now the value is greater than 50 i.e "+ str(i))
    
#printing content of list using while loop
a = ['1','2']
i = 0 
while(i<len(a)):
    print(a[i])
    i = i+1
#printing content of list using for loop
a =['1','2']
 
for list in a:
    print(list)
#range fumction in python
for i in range(1, 8):
    print(i) 
# Break statement
for i in range(5):
  print(i)
  if (i == 4):
      break
# Continue(skip statement)
for i in range(10):
 print(i)
 if (i == 5):
     continue
     print(i)
#pass statement(Null Statement)
i = 4
if(i>0):
    pass
print("python is a good language")