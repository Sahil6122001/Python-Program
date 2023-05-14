def vowels_constant(a):
    v = 0
    c = 0
    for i in a:
        if(i=='a' or i=='e' or i =='i' or i=='o' or i =='u'or
        i =='A' or i =='E' or i =='I' or i == 'O' or i =='U'):
             v = v + 1
        else:
             c = c+1
    return(v,c)
a = input()
v,c = vowels_constant(a)
print(v)
print(c)