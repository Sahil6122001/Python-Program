


string=input("Enter string:")
count=0
count1 =0
for i in string:
      if(i.isdigit()):
            count=count+1
print(count)
new_string = ''.join((x for x in string if not x.isdigit()))

print(new_string)
