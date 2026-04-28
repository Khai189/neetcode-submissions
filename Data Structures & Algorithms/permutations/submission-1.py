class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(curr_perm):
            if len(curr_perm) == len(nums):
                res.append(curr_perm.copy())
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr_perm.append(nums[i])
                    
                    dfs(curr_perm)
                    
                    used[i] = False
                    curr_perm.pop()
        
        dfs([])
        return res