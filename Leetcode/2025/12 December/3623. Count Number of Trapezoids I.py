# Problem: https://leetcode.com/problems/count-number-of-trapezoids-i/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a counter to count the frequency of each y-coordinate and then calculate the area of each trapezoid
# Data Structure: Counter

from collections import Counter

class Solution:
    def countTrapezoids(self, points) -> int:
        freq = Counter(p[1] for p in points)
        Sum, c2 = 0, 0
        for f in freq.values():
            if f <= 1: continue
            c = f * (f - 1) // 2
            Sum += c
            c2 += c * c
        return (Sum * Sum - c2) // 2 % (10 ** 9 + 7)
