class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Loop through the array to find the lowest selling price
        to pick a day, it must: 
        1) price not already been seen 
        2) the price must be the lowest within the remaining array
        3) return an integer > 0 
        4) the selling price > buying price

        *** Potential Solutions ***
        #1 
        runtime: O(N^2)
        type: nested for loop using hashmap to keep track of pair

        #2
        use a queue since FIFO
        '''

        maxProfit = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        return maxProfit











