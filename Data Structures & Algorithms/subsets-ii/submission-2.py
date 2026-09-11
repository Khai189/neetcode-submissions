class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(start: int):
            res.append(path.copy())

            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return res