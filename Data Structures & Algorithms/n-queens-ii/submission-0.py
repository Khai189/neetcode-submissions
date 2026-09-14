class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(r):
            if r == n:
                return 1
            
            total_sum = 0
            for c in range(n):
                if c not in cols and r + c not in pos_diag and r - c not in neg_diag:
                    cols.add(c)
                    pos_diag.add(r+c)
                    neg_diag.add(r-c)

                    total_sum += backtrack(r+1)

                    cols.remove(c)
                    pos_diag.remove(r+c)
                    neg_diag.remove(r-c)
            
            return total_sum
                
        
        return backtrack(0)



