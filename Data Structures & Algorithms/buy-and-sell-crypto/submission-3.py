class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lowPrice = 0
        highPrice = 0
        profit = 0
        # [10, 1, 5, 6, 7, 1]
        while highPrice <= len(prices)-1:
            currentProfit = prices[highPrice] - prices[lowPrice]
            if currentProfit < 0:
                lowPrice+=1
            else:
                profit = max(profit, currentProfit)
                highPrice+=1
        return profit

        