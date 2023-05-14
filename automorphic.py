n = 376
print("yes" if int (str(n**2)[-len(str(n))::])==n else "no")
# using endswith()
n = 5
a = str(n)
m = n ** 2
b = str(m)
if b.endswith(a):
    print("automorphic")
else:
    print("non automorphic")