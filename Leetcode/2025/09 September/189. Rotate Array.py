# Problem: https://leetcode.com/problems/rotate-array/
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Use slicing to rotate the array in-place
# Data Structure: List

class Solution:
    def rotate(self, nums, k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]