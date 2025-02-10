# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium
# Approach: Binary Search
# Time Complexity: O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
