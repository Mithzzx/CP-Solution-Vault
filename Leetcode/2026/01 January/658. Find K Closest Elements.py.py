# Problem: https://leetcode.com/problems/find-k-closest-elements/
# Time Complexity: O(n), Space Complexity: O(k)
# Approach: Use a sliding window to keep track of the closest k elements
# Data Structure: List, Algorithm: Sliding Window

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = arr[0:k]
        for i in arr[k:]:
            ld = abs(l[0] - x)
            rd = abs(l[-1] - x)
            cd = abs(i - x)
            if ld > cd or rd > cd:
                l.append(i)
                l.pop(0)
        return l