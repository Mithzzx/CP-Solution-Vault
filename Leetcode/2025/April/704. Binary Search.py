# Problem: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Approach: Use binary search to find the target element
# Time Complexity: O(log n), Space Complexity: O(1)

class Solution:
    def search(self, nums, target):
        def find(t, s, e):
            if s > e:
                return -1
            m = (s + e) // 2
            if nums[m] == t:
                return m
            elif nums[m] > t:
                return find(t, s, m - 1)
            else:
                return find(t, m + 1, e)

        return find(target, 0, len(nums) - 1)
