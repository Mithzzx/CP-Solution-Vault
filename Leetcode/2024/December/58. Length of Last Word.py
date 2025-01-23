class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = True
        c = 0

        for i in range(1, len(s) + 1):
            if w and s[-i] == " ":
                continue
            else:
                w = False
                if s[-i] != " ":
                    c += 1
                else:
                    break
        print(c - 1)


s = Solution()
s.lengthOfLastWord("Hello World")
