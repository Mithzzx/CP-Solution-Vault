#Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Time Complexity: O(n), Space Complexity: O(1)
#Approach: Keep track of the lowest price seen so far and compare it with the current price
#Data Structure: List

class Solution:
    def maxProfit(self, prices):
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)

        return profit