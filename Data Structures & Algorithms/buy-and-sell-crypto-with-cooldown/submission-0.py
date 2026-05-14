class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initial idea: this is essentially a deciision tree.
        # At each stock we are choosing either buy/sell depending on if we have a neetcode or if we dont
        # and alternatively holding out and not performing any action
        # We could try a DFS solution but that would be O(2^n) time and space complexity as we need to recalculate a bunch of previous calculations

        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        return dfs(0, True)
