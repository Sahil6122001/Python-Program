import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol  = "!@$#%^&*()_+-="
all = lower + upper + number+ symbol
length  = 11
password = "".join(random.sample(all,length))
print("the random password you have to put",password)
