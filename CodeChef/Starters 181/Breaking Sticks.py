# Problem: https://www.codechef.com/START181D/problems/BRKSTICK
# Approach: Calculate the maximum number of breaks possible
# Time Complexity: O(n), Space Complexity: O(1)

def max_breaks(sticks):
    total_breaks = 0
    for stick in sticks:
        if stick > 1:
            total_breaks += (stick - 1)
    return total_breaks


t = int(input())

for _ in range(t):
    n = int(input())

    sticks = list(map(int, input().split()))

    print(max_breaks(sticks))