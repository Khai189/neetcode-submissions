class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]

        output = []

        pos_diag = set()
        neg_diag = set()
        cols = set()
        def backtrack(r, board):
            if r == n:
                output.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                
                if c not in cols and r - c not in neg_diag and r + c not in pos_diag:
                    cols.add(c)
                    neg_diag.add(r-c)
                    pos_diag.add(r+c)

                    board[r][c] = "Q"
                    backtrack(r+1, board)
                    board[r][c] = "."

                    cols.remove(c)
                    neg_diag.remove(r-c)
                    pos_diag.remove(r+c)
        
        backtrack(0, board)
        return output
