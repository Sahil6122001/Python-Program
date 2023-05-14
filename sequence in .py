def issequence(num):
    if(num in '123456789'):
        return True
    else:
        return False
num = input()
print(issequence(num))
