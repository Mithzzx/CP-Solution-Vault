class Solution:
    def makeGood(self, s: str) -> str:
        lis = list(s)
        lp = 0

        while lp+1 < len(lis) and lis:
            diff = ord(lis[lp]) - ord(lis[lp+1])
            if diff in (32,-32):
                lis.pop(lp+1)
                lis.pop(lp)
                lp = 0
                continue
            else:
                lp+=1

        return "".join(lis)