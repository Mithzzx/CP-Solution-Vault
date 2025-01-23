class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base(x, y):
            s = ""
            while y > 0:
                r = y % x
                y = int(y / x)
                s += str(r)
            return s

        n = 9
        palindrome = False
        for i in range(2, n - 1):
            b = base(i, 9)
            if b == b[::-1]:
                palindrome = True
            else:
                palindrome = False
                break

        return palindrome

