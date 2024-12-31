class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights.copy()
        exp.sort()
        x = 0
        for ind, i in enumerate(heights):
            if i != exp[ind]:
                x += 1
        return x

