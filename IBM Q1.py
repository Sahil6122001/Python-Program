a = "011000100000110100100000"
if len(a)%4!=0:
	print("invalid input")
else:
	lst = ['0','1','2','3','4','5','6','7','8','9''+','-','*','/']
for i in range(0,len(a),+4):
    temp = a[i:i+4]
    btd = int(temp,2)
    p = lst[btd]
    if p=='+' or p =='-' or p =='*' or p =='/':
        print()
        print(p)
    else:
    	print(p,end="")