names = []
scores=[]
n = int(input())
for i in range(n):
    name = input()
    score = input()
    names.append(name)
    scores.append(score)
a = list(set(scores))
a.sort()  
result = a[1]
result = [names[i] for i in range(n) if scores[i] == result]
result.sort()
for person in result:
    print(person)