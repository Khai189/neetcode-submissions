class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        curSub = []
        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    res.append(curSub.copy())
                return
            
            if self.isPali(s, j, i):
                curSub.append(s[j : i + 1])
                backtrack(i+1, i+1)
                curSub.pop()
            
            backtrack(j, i+1)

        backtrack(0, 0)
        return res
        
    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True
