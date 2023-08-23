def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    mutate_string = "".join(string)
    return mutate_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# second method
s = list(int(input()))
character = input()
i = int(input())
s[i] = character
s = "".join(s)
print(s)
# string .replace
txt = " my name is sahil"
a = txt.replace("sahil","saurav")
print(a)