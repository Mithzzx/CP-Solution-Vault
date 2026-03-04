#Problem Link: https://leetcode.com/problems/simplify-path/
#Time Complexity: O(n), Space Complexity: O(n)
#Approach: Use a stack to store the directory names
#Data Structure: Stack, Algorithm: Stack

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for i in path.split("/"):
            if i == ".." and s:
                s.pop()
            elif i == '' or i == '.' or i == '..':
                continue
            else:
                s.append(i)
        return '/' + '/'.join(s)
