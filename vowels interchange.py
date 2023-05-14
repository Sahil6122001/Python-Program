s = input()
s = s.replace('u','a').replace('o','u').replace('i','o').replace('e','i').replace('a','e')
position = 4
new_character = 'a'

s = s[:position] + new_character + s[position+1:]
print(s)