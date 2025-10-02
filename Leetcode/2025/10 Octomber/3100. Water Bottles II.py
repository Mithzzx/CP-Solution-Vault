# Problem: https://leetcode.com/problems/water-bottles-ii/
# Time Complexity: O(log n), Space Complexity: O(1)
# Approach: Keep subtracting x - 1 from numBottles until numBottles < x
# Data Structure: None

class Solution(object):
    def maxBottlesDrunk(self, numBottles, x):
        ans = numBottles
        while numBottles >= x:
            numBottles -= x - 1
            x += 1
            ans += 1
        return ans