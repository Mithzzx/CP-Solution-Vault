t = int(input())
for _ in range(t):
    l = int(input())
    s = input()
    print('No' if len(s) == len(set(s)) else "Yes")
