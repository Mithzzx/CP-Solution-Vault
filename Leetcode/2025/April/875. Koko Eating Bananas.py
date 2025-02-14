# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Approach: Binary Search
# Time Complexity: O(n * log(max(piles)))

class Solution:
    def check(self, piles, h, mid):
        ans = 0
        for pile in piles:
            ans += pile // mid
            if pile % mid != 0:
                ans += 1
        return 1 if ans <= h else 0

    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) >> 1
            if self.check(piles, h, mid) == 1:
                high = mid
            else:
                low = mid + 1
        return low