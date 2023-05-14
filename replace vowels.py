
str = input()


char = input()

newstr = ""
for i in range(len(str)):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='A' or str[i]=='E'or str[i]=='I'or str[i] =='O' or str[i]=='U':
        newstr = newstr + char
    else:
        newstr = newstr + str[i]

print("Original String:", str)
print("New String:", newstr)