import sys

v = sys.stdin.read().split()
t = int(v[0])
p = 1
for _ in range(t):
    n = int(v[p])
    a = list(map(int, v[p + 1: p + n + 2]))
    p += n + 2

    res = min(max(a[i], a[i + 1]) for i in range(n))
    print(res)
