class Solution:
    def __init__(self):
        self.power = None
        self.score = None

    def bagOfTokensScore(self, tokens: list[int], power: int):
        self.power = power
        self.score = 0
        tokens.sort()

        def faceup():
            self.power -= tokens.pop(0)
            self.score += 1

        def facedown():
            self.power += tokens.pop(-1)
            self.score -= 1

        while len(tokens) != 0:
            if self.power >= tokens[0]:
                faceup()
            elif len(tokens) != 1:
                facedown()
            else:
                tokens.pop(0)
        return self.score


S = Solution()
print(S.bagOfTokensScore([100, 200, 300, 400], 200))
print(S.bagOfTokensScore([71, 55, 82], 54))
