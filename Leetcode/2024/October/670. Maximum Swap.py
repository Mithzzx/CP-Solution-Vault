num = 2736
#Output: 7236
x=[list(str(num))]
last = {int(d): i for i, d in enumerate(str(num))}
print(last)