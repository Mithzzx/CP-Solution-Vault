n = int(input())
groups = list(map(int, input().split()))

c1 = c2 = c3 = c4 = 0
for g in groups:
    if g == 1:
        c1 += 1
    elif g == 2:
        c2 += 1
    elif g == 3:
        c3 += 1
    else:
        c4 += 1

taxis = c4

pairs = min(c3, c1)
taxis += c3
c1 -= pairs

taxis += c2 // 2
if c2 % 2:  # one group of 2 left
    taxis += 1
    c1 -= min(2, c1)  # fill with up to 2 ones

if c1 > 0:
    taxis += (c1 + 3) // 4  # ceil(c1/4)

print(taxis)