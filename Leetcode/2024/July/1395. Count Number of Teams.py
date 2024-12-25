class Solution:
    def numTeams(self, rating: List[int]) -> int:
        y = [rating, rating[::-1]]
        x = 0
        for o in y:
            for ind, i in enumerate(o):
                for j in range(ind, len(o)):
                    if o[j] < i:
                        i2 = o[j]
                        for k in range(j, len(o)):
                            if o[k] < i2:
                                x += 1

        return x