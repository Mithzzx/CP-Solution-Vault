# Problem: https://codeforces.com/problemset/problem/266/A
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Iterate through the list and count consecutive identical characters
# Data Structure: List

n = int(input())
arr = list(input())
x = -1
current = arr[0] if arr else None
for i in arr:
    if current == i:
        x += 1
    current = i
print(x)