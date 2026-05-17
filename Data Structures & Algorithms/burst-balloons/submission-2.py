class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # This is a maximum amount of profit question
        # OHHH we have two decisiojns at each balloon
        # We choose to pop the balloon or not pop the balloon
        # If we pop the balloon, we add to our coin count the product
        # This can also be helped with Top-Down DP
        # But wait we change each of the sub problems each decision we make
        # Therefore we can't do it with traditional DP
        # We need to take the maximum output possible and work backwards so further decisions aren't impacted
        # This means we need a bottom-up solution where we work from the back of the array
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]