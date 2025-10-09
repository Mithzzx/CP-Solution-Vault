t = int(input())
for _ in range(t):
    n = input()
    s = input()
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == '0':
            l += 1
        elif s[r] == '0':
            r -= 1
        if s[l] == '1' and s[r] == '1': break

    c = 0
    for i in range(l + 1, r):
        if s[i] == '0':
            c += 1
    print(c)