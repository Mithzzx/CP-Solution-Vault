import sys

v = sys.stdin.read().split()
t = int(v[0])
p = 1
for _ in range(t):
    n = int(v[p])
    r1 = list(map(int, v[p + 1: p + n + 1]))
    r2 = list(map(int, v[p + n + 1: p + 2 * n + 1]))
    p += 2 * n + 1

    f = [0] * n
    f[0] = min(r1[0], r2[0])
    for i in range(1, n):
        lo, hi = min(r1[i], r2[i]), max(r1[i], r2[i])
        if lo >= f[i - 1]:
            f[i] = lo
        elif hi >= f[i - 1]:
            f[i] = hi
        else:
            f[i] = 10 ** 18

    s = [0] * n
    s[n - 1] = max(r1[n - 1], r2[n - 1])
    for i in range(n - 2, -1, -1):
        lo, hi = min(r1[i], r2[i]), max(r1[i], r2[i])
        if hi <= s[i + 1]:
            s[i] = hi
        elif lo <= s[i + 1]:
            s[i] = lo
        else:
            s[i] = -10 ** 18

    ok = False
    for i in range(n):
        for u, d in [(r1[i], r2[i]), (r2[i], r1[i])]:
            c1 = (i == 0 or u >= f[i - 1])
            c2 = (d >= u)
            c3 = (i == n - 1 or d <= s[i + 1])
            if c1 and c2 and c3:
                ok = True
                break
        if ok: break

    print("Yes" if ok else "No")