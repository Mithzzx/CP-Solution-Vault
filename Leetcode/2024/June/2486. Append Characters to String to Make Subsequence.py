class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sl = [x for x in s]
        x = 0

        for ind, target in enumerate(t):
            print(target, "::")
            if target in sl:
                print(target, "=", sl)
            else:
                x = len(t) - ind
                break

        return x