class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Brute force solution would be a dfs algorithim that has 2 choices at each turn
        # This would result in O(2^n) time complexity and due to recursion stacks O(n) memory
        # However, we can optimize this problem
        # The question here is if we had a list of 4 numbers
        # we add the first two which would result in 3 different outcomes 
        # The question is we can actually do backwards with a dynampic programming approach
        # We can pass down the 
        dp = {}
        def dfs(total, i):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = dfs(total-nums[i], i+1) + dfs(total+nums[i], i+1)

            return dp[(i, total)]
        
        return dfs(0, 0)