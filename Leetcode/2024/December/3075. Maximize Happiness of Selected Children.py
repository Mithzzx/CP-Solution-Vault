happiness = [12,1,42]
k = 3
happiness.sort(reverse=True)

c = 0
for i in range(k):
    if happiness[i] - i < 0:
        break
    c += (happiness[i] - i)

print(c)
