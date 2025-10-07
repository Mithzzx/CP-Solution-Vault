x = input()
ons = 0
zrs = 0
m = 0
for i in x:
    if i == "1":
        ons += 1
        zrs = 0
    else:
        zrs += 1
        ons = 0
    m = max(m, zrs,ons)
print("YES" if m >= 7 else "NO")