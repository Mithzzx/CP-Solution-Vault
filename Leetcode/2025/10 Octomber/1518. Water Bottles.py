# Problem: https://leetcode.com/problems/water-bottles/
# Time Complexity: O(log n), Space Complexity: O(1)
# Approach: Keep exchanging the empty bottles until we can't exchange anymore
# Data Structure: None

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        x = numBottles
        while numBottles >= numExchange:
            r = numBottles % numExchange
            numBottles = numBottles // numExchange
            x += numBottles
            numBottles += r

        return x
