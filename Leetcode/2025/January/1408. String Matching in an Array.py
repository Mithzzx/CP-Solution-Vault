words = ["leetcoder","leetcode","od","hamlet","am"]
l = len(words)
words.sort(key=len)

print(words)
x=[]
for ind, i in enumerate(words):
    for j in range(ind+1, l):
        if i in words[j]:
            x.append(i)
            break
print(x)

