#Problem link: https://leetcode.com/problems/count-number-of-nice-subarrays/
#Time Complexity: O(n), Space Complexity: O(n)
#Approach: Use a sliding window to count the number of subarrays with a given sum
#Data Structure: List, Algorithm: Sliding Window

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        cnt = [0] * (n + 1)
        cnt[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += cnt[t - k]
            cnt[t] += 1
        return ans
