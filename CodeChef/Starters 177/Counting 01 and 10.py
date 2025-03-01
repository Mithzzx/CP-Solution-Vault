# Problem: Counting 01 and 10
# Link: https://www.codechef.com/START177B/problems/COUNT0110
# Time Complexity: O(N)
# Space Complexity: O(1)
# Approach: For each possible value of C1, calculate the number of 01 and 10 pairs that can be formed

def solve(n):
    half = n // 2
    ans = 0

    for C1 in range(half + 1):
        m = C1 * (n - C1)
        ans += m + 1
    return ans


T = int(input())

for _ in range(T):
    N = int(input())
    result = solve(N)
    print(result)