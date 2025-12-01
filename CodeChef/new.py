t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = map(int, input().split())

    has_small = False
    has_large = False
    has_equal = False

    for val in a:
        if val < x: has_small = True
        elif val > x: has_large = True
        else: has_equal = True

        if has_small and has_large and not has_equal: print("No")
        else: print("Yes")