n = int(input())
numbers = list(map(int, input().split()))


evenness = [num % 2 for num in numbers]

if evenness[:3].count(0) > 1:
    for i in range(n):
        if numbers[i] % 2 != 0:
            print(i + 1)
            break
else:
    for i in range(n):
        if numbers[i] % 2 == 0:
            print(i + 1)
            break
