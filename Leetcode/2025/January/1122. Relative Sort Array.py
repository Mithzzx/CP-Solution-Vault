arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]

dic = {}
x=[]
d=[]
for i in arr1:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for j in arr2:
    x.extend([j]*dic.pop(j))

for key in dic:
    d.extend([key]*dic[key])
d.sort()
x.extend(d)

print(x)
