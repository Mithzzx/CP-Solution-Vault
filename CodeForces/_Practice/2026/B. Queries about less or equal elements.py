n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

results = []

for val in b:
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= val:
            low = mid + 1
        else:
            high = mid
    results.append(low)

print(*results)