def s():
    n = int(input())
    p = list(map(int, input().split()))
    x = input()

    i1 = -1
    iN = -1

    for i in range(n):
        if p[i] == 1:
            i1 = i + 1
        if p[i] == n:
            iN = i + 1

    if x[i1 - 1] == '1' or x[iN - 1] == '1':
        print(-1)
        return

    if x[0] == '1' or x[n - 1] == '1':
        print(-1)
        return

    ops = [
        (1, i1),
        (i1, n),
        (1, iN),
        (iN, n)
    ]

    print(4)
    for l, r in ops:
        print(f"{l} {r}")


t = int(input())
for _ in range(t):
    s()