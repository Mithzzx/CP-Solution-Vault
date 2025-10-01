# Problem: https://leetcode.com/problems/find-pivot-index/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Precompute the prefix sums from left and right and compare them
# Data Structure: List, prefix sum

class Solution(object):
    def pivotIndex(self, nums):
        rps = []
        lps = []
        x = 0
        for i in nums:
            x += i
            rps.append(x)

        x = 0
        for i in range(len(nums) - 1, -1, -1):
            x += nums[i]
            lps.append(x)

        i = 0
        while i < len(nums):
            left = 0 if i == 0 else rps[i - 1]
            right = 0 if i == len(nums) - 1 else lps[len(nums) - 1 - i - 1]
            if left == right:
                return i
                break
            i += 1
        return -1