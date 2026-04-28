class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        curSub = []
        def dfs(i, curSub, target):
            if target == 0:
                res.append(curSub.copy())
                return
            elif i>= len(candidates)or target < 0:
                return 
            curSub.append(candidates[i])
            dfs(i + 1, curSub, target - candidates[i])
            curSub.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            dfs(i + 1, curSub, target)
        dfs(0, [], target)

        return res

