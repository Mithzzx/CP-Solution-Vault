digits = [2,1,3,0]
digits.sort()
print(digits)

n = 0
x=[]

for i in range(len(digits)):
    if digits[i] == 0: continue
    n = digits[i]*100
    for j in range(len(digits)):
        if j == i: continue
        n += digits[j]*10
        for k in range(len(digits)):
            if k == i or k == j or digits[k]%2 != 0: continue
            n += digits[k]
            x.append(n)
            n -= digits[k]
        n -= digits[j] * 10

print(x)

