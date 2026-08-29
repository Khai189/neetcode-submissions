class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # prices = [1, 3, 4, 0, 4]
        # profit = 6
        # The best choices here are to buy on day 1, sell on day 1, buy on day 3, then buy on day 4
        # We have a choice at each price, do we buy or do we sell
        # If we've sold we need to buy again with a new cooldown in place 
        # How do we account for the cooldown in turns of splitting up this problem into smaller bits?
        # We ask ourselves if we're holding a stock and thats how we calculate it or if we rest or if we sell

        held = float("-inf")
        sell = 0
        rest = 0

        for price in prices:
            prev_held = held
            prev_sell = sell
            prev_rest = rest

            held = max(-price + prev_rest, prev_held)
            sell = price + prev_held
            rest = max(prev_sell, prev_rest)





        return max(sell, rest)
