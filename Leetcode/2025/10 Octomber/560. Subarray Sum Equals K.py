# Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a hashmap to store the prefix sums and their counts
# Data Structure: Hashmap, Algorithm: prefix sum

class Solution(object):
    def subarraySum(self, nums, k):
        ps = {}
        sum,x = 0,0

        for i in nums:
            sum +=i
            if sum == k:
                x += 1
            if sum-k in ps:
                x += ps[sum-k]
            ps[sum] = ps.get(sum,0)+1
        return x