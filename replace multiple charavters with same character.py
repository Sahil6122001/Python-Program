str = 'python'
indexes = [2,4,5]
new_character = 'a'
result = ''
for i in indexes:
    str = str[:i]+new_character+str[i+1:]
print(str)