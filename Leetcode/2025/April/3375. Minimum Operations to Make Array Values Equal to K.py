# Problem: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description
# Difficulty: Easy
# Approach: Use a set to store unique values greater than k
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
