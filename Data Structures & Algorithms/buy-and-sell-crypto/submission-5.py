class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy, sell = 0, 1
        profit = 0
        n = len(prices)

        while sell < n:
            curr_profit = prices[sell] - prices[buy]
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                profit = max(profit, curr_profit)
                sell += 1
        return profit