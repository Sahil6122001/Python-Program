def is_leap(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))
# point to be noted that in this code we have use opeartors in descending order for proper working always use arithmetic operator in re
##verse order##