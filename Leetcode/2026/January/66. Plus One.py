#Problem : https://leetcode.com/problems/plus-one/
#Time Complexity: O(n), Space Complexity: O(1)
#Approach: Iterate through the list from the end and increment the number at each index
#Data Structure: List

class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits