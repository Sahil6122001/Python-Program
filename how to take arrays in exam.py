n = int(input())
list_items = list(map(int,input().split(' ')))

for i in list_items:
   print(list_items,end =" ")
# 2 method
from array import *
num = array('i', [])
n = int(input())

for i in range(n):
    n.append(int(input()))

for i in range(len(n)):
    print(n[i])