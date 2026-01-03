# Problems: https://leetcode.com/problems/contains-duplicate-ii/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a dictionary to store the last seen index of each number and check the distance
# Data Structure: Dictionary, Algorithm: Sliding Window

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False