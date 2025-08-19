# Problem: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Approach: Use two pointers to move non-zero elements to the front and fill the rest with zeros
# Time complexity: O(n), Space complexity: O(1)

class Solution:
    def moveZeroes(self, nums) -> None:
        l,r = 0,1
        while r < len(nums):
            if nums[l] == 0 and nums[r] == 0:
                r+=1
                continue
            if nums[l]==0:
                nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r+1
