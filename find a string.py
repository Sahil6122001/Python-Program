def count(string,sub_string):
    count = 0
    start =0
    while(start<len(sub_string)):
        index = string.find(string,start)
        if index == -1:
            break
        start = index+1
        count +=1
    return count
string = input().strip()
sub_string = input().strip()
print(count(string,sub_string))