_ = int(input())
for i in range(_):
    a,b,n,s = map(int, input().split())
    if s // n <= a and s % n <= b:
        print("YES")
    elif s // n > a and b >= s - (a * n):
        print("YES")
    elif b >= s:
        print("YES")
    else:
        print("NO")
