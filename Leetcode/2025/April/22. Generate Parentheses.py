# Problem: https://leetcode.com/problems/generate-parentheses/
# Difficulty: Medium
# Approach: Backtracking
# Time Complexity: O(4^n / sqrt(n)), Space Complexity: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return

            if openP < n:
                dfs(openP + 1, closeP, s + "(")

            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")
        return res