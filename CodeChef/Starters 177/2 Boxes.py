# Problem: Starters177B 2 Boxes
# Link: https://www.codechef.com/START177B/problems/BOX2
# Time Complexity: O(1)
# Space Complexity: O(1)
# Approach: Calculate the difference between the two boxes and the key, then divide by 2

t = int(input())
for _ in range(t):
    x, y, k = map(int, input().split())
    d = abs(x - y)
    e = abs(d - k)
    print(e // 2 if (e / 2) == (e // 2) else -1)