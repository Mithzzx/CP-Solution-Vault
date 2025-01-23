words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]

x=set(words1)
letters = {}
for i in words2:
    for j in i:
        count = i.count(j)
        if j not in letters or count > letters[j]:
            letters[j] = count
for i in words1:
    for j in letters:
        if i.count(j) < letters[j]:
            x.remove(i)
            break

print(x)