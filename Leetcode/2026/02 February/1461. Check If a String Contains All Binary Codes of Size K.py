class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        for i in range(0, len(s)):
            if len(s[i:i + k]) == k:
                d.add(s[i:i + k])

        return len(d) == 2 ** k
