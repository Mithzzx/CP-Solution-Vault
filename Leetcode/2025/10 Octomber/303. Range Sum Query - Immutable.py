#Problem Link: https://leetcode.com/problems/range-sum-query-immutable/
#Time Complexity: O(1) for sumRange, O(n) for initialization, Space Complexity: O(n)
#Approach: Precompute the prefix sums and use them to get the sum in O(
#Data Structure: List


class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        x = 0
        for i in nums:
            x += i
            self.prefix.append(x)

    def sumRange(self, left, right):
        return self.prefix[right] - (0 if left == 0 else self.prefix[left - 1])
