import datetime
currentTime = datetime.datetime.now()
currentTime.hour

n = input("enter your name")
if currentTime.hour<12:
    print("good morning",n)
elif 12<=currentTime.hour<18:
    print("good afternoon",n)
else:
    print("good evening",n)