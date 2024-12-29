class Solution:
    def longestPalindrome(self, s: str)
        lis = {x: int(s.count(x)) for x in s}
        l = list(lis.values())
        single = True
        x = 0
        for i in l:
            if i >= 2:
                r = i % 2
                x += (i - r)
                i = r
            if single and i == 1:
                single = False
                x += 1
        return x