def password(encoded_string):
    rev = encoded_string[::-1]
    
    password = " "
    i = 0
    while i< len(rev):
        if i +2 <=len(rev)  and  int(rev[i:i+2]) >= 65 and int(rev[i:i+2]) <=122:
            password += chr(int(rev[i:i+2]))
            i +=2
        elif i + 3 <= len(rev) and int(rev[i:i+3]) >= 65 and int(rev[i:i+3]) <=122:
            password += chr(int(rev[i:i+3]))
            i += 3
        else:
            i += 1
    return password
    
encoded_string = input()
password = password(encoded_string)
print(password)        
#input will be 796115110113721110141108
