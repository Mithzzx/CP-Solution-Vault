#Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Approach: Use two pointers to reverse the string in place
# Time complexity: O(n), where n is the length of the string

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        slow=0
        for fast in range(slow+1,len(nums)):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1