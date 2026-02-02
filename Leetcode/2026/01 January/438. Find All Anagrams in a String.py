# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a sliding window to count the frequency of each character in the window
# Data Structure: Dictionary, Algorithm: Sliding Window

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)

        p_count = Counter(p)
        window_count = Counter(s[:p_len - 1])
        res = []

        for i in range(p_len - 1, s_len):
            window_count[s[i]] += 1

            if window_count == p_count:
                res.append(i - p_len + 1)

            left_char = s[i - p_len + 1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

        return res