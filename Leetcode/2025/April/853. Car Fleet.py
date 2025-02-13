#Problem: https://leetcode.com/problems/car-fleet/
# Difficulty: Medium
# Approach: Use a dictionary to store the time taken for each car to reach the target
# Time Complexity: O(n log n), Space Complexity: O(n)

class Solution:
    def carFleet(self, target: int, position, speed):
        d,g,c = {},0,0
        for ind,i  in enumerate(position):
            d[i] = (target-i)/speed[ind]
        position.sort(reverse=True)
        l = [d[x] for x in position]
        for i in l:
            if i > g: c,g = c+1,i
        return c