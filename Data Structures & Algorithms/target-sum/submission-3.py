class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, cur_sum):
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            elif i == len(nums):
                return 1 if cur_sum == target else 0
            
            cur_num = nums[i]
            add = dfs(i+1, cur_sum + cur_num)
            sub = dfs(i+1, cur_sum - cur_num)
            
            memo[(i, cur_sum)] = add + sub

            return memo[(i, cur_sum)]
        
        return dfs(0, 0)


            
