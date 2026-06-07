class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, len(prices) - 1

        maxProfit = 0

        lowest = prices[0]

        for p in prices:
            if p < lowest:
                lowest = p
            maxProfit = max(maxProfit, p -  lowest)
        return maxProfit

        