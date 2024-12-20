class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        t = 0
        g = 0
        for ind,i in enumerate(tickets):
            if i < x:
                t += i
            else:
                t += x
            if ind > k and i > x:
                g+=1
        return t-g
