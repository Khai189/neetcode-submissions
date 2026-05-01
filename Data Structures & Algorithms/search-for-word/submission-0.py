class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (c < 0 or r < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c] or board[r][c] == "#"):
                return False 

            board[r][c] = "#"
            res = (
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1) or
                backtrack(r, c+1, i+1) or
                backtrack(r, c-1, i+1)
            )
            board[r][c] = word[i]
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        
        return False
            
