class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur_visit = set()

        def backtrack(path):

            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num not in cur_visit:
                    cur_visit.add(num)
                    path.append(num)

                    backtrack(path)

                    path.pop()
                    cur_visit.remove(num)
            
        backtrack([])
        return res