# to read the content of the file
f = open('sampe.txt','r')
data = f.read()
print(data)
f.close

# use of readline
f =  open('sampe.txt')
#read 1 line
data = f.readline()
print(data)
#read 2 line
data = f.readline()
print(data)
f.close
# write in a file
f = open('another.txt','w')
f.write("please write here")
f.close
#appending a file
f  = open('another.txt','a')
f.write("i am appending")
f.close
# with statement 
with open('another.txt','r') as f :
 f.read()
