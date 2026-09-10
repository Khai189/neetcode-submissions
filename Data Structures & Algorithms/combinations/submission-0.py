class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def backtrack(ind, used, path):
            if used == 0:
                res.append(path.copy())
                return
            
            elif ind == n+1:
                return
            
            for j in range(ind, n+1):
                path.append(j)
                backtrack(j+1, used-1, path)
                path.pop()
        
        backtrack(1, k, [])
        return res