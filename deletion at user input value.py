def delete(lst, value):
    while value in lst:
        lst.remove(value)

# Example usage
a = [1, 2, 3, 4, 3, 5, 6, 3, 7]
print("Before deletion:", a)

delete(a, 4)
print("After deletion:", a)
#second
def delete(lst, value):
    while value in lst:
        lst.remove(value)
a=[1,2,3,4,5,6]
print("befre deletion", a)
b = int(input("enter the value to be deeted:-"))
if b not in a:
    print("the number you have entered is not in the list")
delete (a,b)
print("After deletion",a)