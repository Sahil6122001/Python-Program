s = input()
c = input()
try:
    index = s.index(c)
    print(index)
except ValueError:
    print("not found")
