class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []
        def dfs(i, current_subset, remaining_target):
            if remaining_target == 0:
                res.append(current_subset.copy())
                return
            if remaining_target < 0 or i >= len(nums):
                return

            current_subset.append(nums[i])
            dfs(i, current_subset, remaining_target - nums[i])

            current_subset.pop()
            dfs(i + 1, current_subset, remaining_target)
        
        dfs(0, comb, target)
        return res