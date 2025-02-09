#Problem: https://leetcode.com/problems/search-a-2d-matrix/description
# Difficulty: Medium
# Approach: Use binary search to find the target element in a 2D matrix
# Time Complexity: O(log(m*n)), Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        def find(t, s, e):
            m = (s + e) // 2
            if s > e:
                return m
            if nums[m] == t:
                return m
            elif nums[m] > t:
                return find(t, s, m - 1)
            else:
                return find(t, m + 1, e)

        nums = [x[0] for x in matrix]
        row = find(target, 0, len(nums) - 1)
        nums = matrix[row]
        col = find(target, 0, len(nums) - 1)

        return True if matrix[row][col] == target else False