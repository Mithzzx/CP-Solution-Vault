# URL: https://www.codechef.com/problems/REMELEM
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Find the minimum and maximum element in the array and check if their sum is less than or equal to k
# Data Structure: Array

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if n == 1: print("YES")
else:
    min_val, max_val = max(arr), min(arr)
    if min_val + max_val <= k: print("YES")
    else: print("NO")