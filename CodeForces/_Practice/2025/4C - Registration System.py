from collections import defaultdict

l = int(input())
n=[]
for _ in range(l):
    n.append(input())

db = defaultdict()
for i in n:
    if i in db:
        print(i+str(db[i]))
        db[i] += 1

    else:
        print("OK")
        db[i] = 1