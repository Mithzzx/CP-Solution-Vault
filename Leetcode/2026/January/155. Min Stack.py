# Problem: https://leetcode.com/problems/min-stack/
# Time Complexity: O(1), Space Complexity: O(n)
# Approach: Use two stacks to store the elements and their minimum values
# Data Structure: Stack

class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.m == []:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))

    def pop(self) -> None:
        self.m.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]