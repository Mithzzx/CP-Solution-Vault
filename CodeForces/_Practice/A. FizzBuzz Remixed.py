t = int(input())
for _ in range(t):
    n = int(input())
    print((n // 15) * 3 + min(n % 15 + 1, 3))
