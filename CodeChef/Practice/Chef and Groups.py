# Problem: Chef and Groups (https://www.codechef.com/problems/GROUPS)
# Approach: Count the number of groups by checking the number of 1s in the string\
# Time Complexity: O(n), Space Complexity: O(1)

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    x, i = 0, 0

    while i < n:
        if s[i] == '1':
            x += 1
            while i < n and s[i] == '1':
                i += 1
        else:
            i += 1

    print(x)