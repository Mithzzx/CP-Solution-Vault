words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]

def isok(x):
    vowels = {'a','e','i','o','u'}
    if x[0] in vowels and x[-1] in vowels:
        return True
    return False

prefix_sum = 0

for ind,i in enumerate(words):
    if isok(i):
        prefix_sum += 1
    words[ind] = prefix_sum

print(words)

x=[]
for q in queries:
    if q[0] == 0:
        print("q",q[1])
        x.append(q[1])
    else:
        x.append(words[q[1]]-words[q[0]])

print(x)
