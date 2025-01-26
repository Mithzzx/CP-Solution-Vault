words = ["a","aba","ababa","aa"]

c=0
for ind, i in enumerate(words):
    for j in words[ind+1:]:
        if (j[:len(i)]==i) and (j[-len(i):] == i):
            c+=1
print(c)
