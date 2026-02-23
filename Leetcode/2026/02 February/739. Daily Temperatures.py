t = [30,40,50,60]
#Output: [1,1,1,0]

s = []
output = [0*i for i in range(len(t))]

for i in range(len(t)):
    while s and t[i] > s[-1][0]:
        ss = s.pop()
        output[ss[1]] = i - ss[1]
    s.append((t[i], i))

print(output)
