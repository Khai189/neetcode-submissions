class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            price = prices[i]

            profit = max(profit, price - buy)

            if price < buy:
                buy = price
            
        return profit