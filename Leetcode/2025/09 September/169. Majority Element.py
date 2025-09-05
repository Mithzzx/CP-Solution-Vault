# Problem link: https://leetcode.com/problems/majority-element/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Count the frequency of each element and return the element with frequency greater than n/2
# Data Structure: Dictionary

class Solution:
    def majorityElement(self, nums) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        m = 0
        for i in d: m = i if d[i] > m else m
        return m