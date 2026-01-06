# Problem link: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/
# Time Complexity: O(n),Space Complexity: O(1)
# Approach: Iterate through the array and check for even-odd alternating subarrays within the threshold
# Data Structure: List, Algorithm: Sliding Window


def longestAlternatingSubarray(nums, threshold):
    n = len(nums)
    max_len = 0
    i = 0

    while i < n:
        if nums[i] % 2 == 0 and nums[i] <= threshold:
            start = i
            i += 1

            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1

            max_len = max(max_len, i - start)
        else:
            i += 1

    return max_len