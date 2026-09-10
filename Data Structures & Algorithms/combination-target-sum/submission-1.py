class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []
        def backtrack(i, cur_sum, path):
            if cur_sum == target:
                output.append(path.copy())
                return
            elif i == len(nums):
                return
            
            for j in range(i, len(nums)):
                
                if cur_sum + nums[j] <= target:
                    path.append(nums[j])
                    backtrack(j, cur_sum + nums[j], path)
                    path.pop()


        
        backtrack(0, 0, [])
        return output


        
