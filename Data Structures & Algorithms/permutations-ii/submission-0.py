class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        cur_visit = set()
        output = []
        def backtrack(path):
            if len(path) == len(nums):
                output.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i in cur_visit:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in cur_visit:
                    continue

                cur_visit.add(i)
                path.append(nums[i])

                backtrack(path)

                path.pop()
                cur_visit.remove(i)
        
        backtrack([])
        return output
