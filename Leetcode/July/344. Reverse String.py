#Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Approach: Use two pointers to reverse the string in place
# Time complexity: O(n), where n is the length of the string


from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l,r = l+1,r-1