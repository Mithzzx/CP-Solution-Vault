def solve():
    n = int(input())
    b = list(map(int, input().split()))

    b.sort()

    can_win = True

    for i in range(1, n - 1, 2):
        if b[i] != b[i + 1]:
            can_win = False
            break

    if can_win:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()