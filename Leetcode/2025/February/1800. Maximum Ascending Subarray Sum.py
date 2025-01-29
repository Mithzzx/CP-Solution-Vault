nums = [3,6,10,1,8,9,9,8,9]

max=[]
maxsum = 0
xsum = 0
x=[]
for i in nums:
    if not x or i > x[-1]:
        x.append(i)
        xsum += i
        print(x, xsum,"::")
    else:
        print(x)
        if xsum > maxsum:
            maxsum = xsum
        x=[i]
        xsum = i
if xsum > maxsum:
    maxsum = xsum
print(maxsum)