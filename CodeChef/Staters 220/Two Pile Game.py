import sys

v = sys.stdin.read().split()

t = int(v[0])
idx = 1
for _ in range(t):
    x = int(v[idx])
    y = int(v[idx + 1])
    idx += 2

    if x % 2 == 1:
        print("Alice")
    else:
        print("Bob")