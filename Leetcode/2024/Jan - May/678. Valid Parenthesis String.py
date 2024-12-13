s = "(*)"

x=[]
for i in s:
    if i == '(' or i=='*':
        x.append(i)
    elif x:
        x.pop(-1)
print(x)
if x:
    print(False)
else:
    print(True)