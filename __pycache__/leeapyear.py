a = int(input("enter a year"))
if(a%400==0):
    print(a,"is leap year")
elif(a%100==0):
    print(a,"is not leap year")
elif(a%4==0):
    print(a,"is a leap year")
else:
    print(a,"is not leap year")
    