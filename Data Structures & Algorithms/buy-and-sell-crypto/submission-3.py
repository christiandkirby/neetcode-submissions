class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        min_price = float("inf")

        for price in prices:
            if price - min_price > ans:
                ans = price - min_price
            elif price < min_price:
                min_price = price
            
        return ans