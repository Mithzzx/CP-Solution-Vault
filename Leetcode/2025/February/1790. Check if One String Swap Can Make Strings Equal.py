s1 = "attack"
s2 = "defend"
l = []

for i in range(len(s1)):
    if s1[i] != s2[i]:
        l.append((s1[i], s2[i]))

if len(l) == 2 and (l[0] == l[1][::-1]):
    print(True)
else:
    print(False)