# Problem: 26. Remove Duplicates from Sorted Array
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Use two pointers to iterate through the array and remove duplicates in-place
# Data Structure: Two Pointers

class Solution:
    def removeDuplicates(self, nums):
        l,r,c = 0,1,1
        while r<len(nums):
            if nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l+=1
                c+=1
            r+=1
        return c