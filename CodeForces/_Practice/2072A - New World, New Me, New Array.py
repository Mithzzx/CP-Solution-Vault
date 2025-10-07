t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())

    max_possible = n * p
    min_possible = n * (-p)

    if k > max_possible or k < min_possible:
        print(-1)
        continue

    if k == 0:
        print(0)
    else:
        if abs(k) % p == 0:
            operations = abs(k) // p
        else:
            operations = abs(k) // p + 1

        print(operations if operations <= n else -1)
