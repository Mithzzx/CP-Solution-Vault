#Problem link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
#Time Complexity: O(n),Space Complexity: O(1)
#Approach: Iterate through the list and check if the current element is repeated
#Data Structure: List, Sliding Window

class Solution:
    def repeatedNTimes(self, A: list[int]) -> int:
        for i in range(len(A) - 2):
            if A[i] == A[i + 1] or A[i] == A[i + 2]:
                return A[i]
        return A[-1]
