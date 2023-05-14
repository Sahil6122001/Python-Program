a = [1,2,4]
b = [3,2,4]
def common(a,b):
    c = [ value for value in a if value in b]
    return c
d = common(a,b)
print(d)