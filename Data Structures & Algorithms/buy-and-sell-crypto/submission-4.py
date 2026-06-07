class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: Integer Array
        # Output: Integer

        # Find the cheapest day and sell in the future
        # Track the highest profit, defaults to 0 if there is none

        profit = 0
        min_price = float("inf")

        for price in prices:
            if price < min_price:
                min_price = price
                continue
            else:
                curr_profit = price - min_price
                profit = max(profit, curr_profit)
        return profit