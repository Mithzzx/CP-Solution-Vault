# Problem: https://leetcode.com/problems/longest-harmonious-subsequence/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a dictionary to count the frequency of each number
# Data Structure: Dictionary, Algorithm: Hash Map

from collections import Counter


def findLHS(nums):
    counts = Counter(nums)
    max_length = 0

    for num in counts:
        if num + 1 in counts:
            current_length = counts[num] + counts[num + 1]
            max_length = max(max_length, current_length)

    return max_length