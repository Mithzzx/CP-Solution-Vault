#Problem Link: https://leetcode.com/problems/find-closest-person/
#Time Complexity: O(1), Space Complexity: O(1)
#Approach: Compare the absolute difference between x and z, and y and z

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) == abs(y - z): return 0
        return 1 if abs(x - z) < abs(y - z) else 2
