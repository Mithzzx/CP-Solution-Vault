#Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Approach: Use two pointers to reverse the string in place
# Time complexity: O(n), where n is the length of the string

class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
