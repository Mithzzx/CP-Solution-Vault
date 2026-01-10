#Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Approach: Use sets to find the intersection of two arrays
# Time complexity: O(n + m), where n and m are the lengths of the two arrays

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        x=[]
        for i in nums1:
            if i in nums2:
                x.append(i)
        return x