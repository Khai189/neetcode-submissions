class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            target_char = word[i]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == target_char:          
                    temp = board[r][c]
                    board[r][c] = "#"
                    if backtrack(nr, nc, i+1):
                        return True
                    
                    board[r][c] = temp
                
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 1):
                        return True
                    
        
        return False
            
