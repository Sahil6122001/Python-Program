def armstrong(a,b):
    if(sorted(a)==sorted(b)):
        return True
    else:
        return False
a = input()
b = input()
print(armstrong(a,b))
