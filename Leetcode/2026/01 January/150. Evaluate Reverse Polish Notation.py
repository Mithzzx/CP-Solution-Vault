# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Use a stack to evaluate the expression
# Data Structure: Stack, Algorithm: Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens) -> int:
        s = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                s.append(int(i))
            else:
                b = s.pop()
                a = s.pop()
                if i == "+":
                    s.append(a + b)
                elif i == "-":
                    s.append(a - b)
                elif i == "*":
                    s.append(a * b)
                else:
                    s.append(int(a / b))
        return s[0]      