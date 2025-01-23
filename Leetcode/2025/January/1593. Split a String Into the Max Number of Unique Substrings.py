s = "ababbccc"
x=set()
d=set()
for i in range(0, len(s)):
    for j in range(i+1, len(s)):
        print(s[i:j])
        if j-1 > i:
            print(s[j - 1], "::")
print(d)