n = int(input("Enter the number of rows"))  
ascii_value = 97
for i in range(n,0,-1):  
        for j in range(0,i):  
           alphabet = chr(ascii_value)
           ascii_value+=1
           print(alphabet,end="")       
        print() 