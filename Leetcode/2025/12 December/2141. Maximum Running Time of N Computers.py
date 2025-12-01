# Problem: https://leetcode.com/problems/maximum-running-time-of-n-computers/
# Time Complexity: O(nlogn), Space Complexity: O(1)
# Approach: Sort the array and keep removing the largest element until the sum of the remaining elements is divisible by n
# Data Structure: List

class Solution:
    def maxRunTime(self, n, arr) :
        arr.sort()
        total = sum(arr)

        while arr[-1] > total // n:
            n -= 1
            total -= arr.pop()

        return total // n
