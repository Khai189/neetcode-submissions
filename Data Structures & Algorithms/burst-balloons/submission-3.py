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
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)