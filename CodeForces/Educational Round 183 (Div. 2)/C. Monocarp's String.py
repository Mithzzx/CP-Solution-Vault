for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    d = set()
    for i in range(len(s)):
        if s[i] == "a":
            c += 1
        else:
            c -= 1
        if i == len(s) - 1: break
        d.add(c)

    if c in d:
        print(c)
    else:
        print(-1)

