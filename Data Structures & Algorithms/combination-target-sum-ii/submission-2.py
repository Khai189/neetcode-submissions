class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur_sum, path):
            if cur_sum == target:
                res.append(path.copy())
                return

            
            for j in range(i, len(candidates)):
                if candidates[j] + cur_sum > target:
                    break
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                backtrack(j+1, cur_sum+candidates[j], path)
                path.pop()

        backtrack(0, 0, [])
        return res
