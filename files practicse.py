# poem word found

with open('poem.txt','r') as f:
    t = f.read()
    if ('twinkle') in t:
        print('yes')
    else:
        print("no")
               

